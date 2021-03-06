from pepperadmin.models import *
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt
import peppertools.settings
from django.db.models import Max
from django.http import JsonResponse
'''
from rest_framework_jwt.settings import api_settings



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
'''


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'code']

class ProcessoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processo
        fields = ('id', 'procname','Tempo_Objetivo',)



class HistoricoSerializer(serializers.ModelSerializer):
    #ostok = serializers.SerializerMethodField(read_only=True)
    
    def create(self, data):
        user = self.context['request'].user
        osedit = None
        osget = None
        edinicio, edfim, edproc = None, None, None
        # print(self.user)
       
        try:
            allos = Historico_Os.objects.filter(os=data["os"], processo=data['processo'])
            period = allos.aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(os=data["os"], processo=data['processo'], periodo=period['periodo__max'])
        except Exception as e:
            print(e) 
       
        if osget:
            edfim = osget.fim
            edinicio = osget.inicio
            edproc = osget.processo
        
        if edfim and 'inicio' in data:
            # se estiver finalizado criar outro 
            print(f"periodos: {period}")
            data['periodo'] = period['periodo__max'] + 1
            periodoprint= data['periodo']
            hist_os = Historico_Os.objects.create(inicio=data['inicio'], periodo=data['periodo'], qtd=data['qtd'], os=data["os"], processo=data['processo'], colaborador=user)
            return hist_os

        elif edinicio and 'fim' in data:
            Historico_Os.objects.filter(os=data["os"], periodo=period['periodo__max'], processo=data['processo']).update(ocorrencias=data["ocorrencias"], fim=data["fim"] )
            hist_os =  Historico_Os.objects.get(os=data["os"], periodo=period['periodo__max'], processo=data['processo'])
            return hist_os
        elif not edfim and 'inicio' in data:
           hist_os = Historico_Os.objects.create(inicio=data['inicio'], periodo=1, qtd = data['qtd'] if 'qtd' in data else 0, os=data["os"], processo=data['processo'], colaborador=user)
           return hist_os
        
    def validate(self, data):
        if not data['processo']:
            raise serializers.ValidationError("Processo n??o encontrado.")
        elif not data['os']:
            raise serializers.ValidationError("Ordem de Servi??o n??o encontrada.")
            
        allos = Historico_Os.objects.filter(os=data["os"], processo=data['processo']).exists()
        osget, prochere, osinicio, osfim = None, None, None, None
        if allos:
            period = Historico_Os.objects.filter(os=data["os"], processo=data['processo']).aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(periodo=period['periodo__max'], processo=data['processo'], os=data["os"])
            prochere = osget.processo
            #proc = Processo.objects.get(pk=osget.processo.id)
            osinicio = osget.inicio
            osfim = osget.fim
           
        if osget and 'fim' in data and not osget.inicio:
            # o.s exists but not ended
            raise serializers.ValidationError("Processo da O.S n??o iniciado.")
        
        elif osget and 'fim' in data and prochere.id != data['processo'].id:
            raise serializers.ValidationError(f"O.S iniciada em {prochere}.")

        elif 'fim' in data and osfim:
            raise serializers.ValidationError(f"O.S j?? finalizada em {prochere}.")
        elif 'fim' in data and not allos:
            # o.s does not exist and not initialized
            raise serializers.ValidationError("O.S n??o iniciada.")
        elif 'inicio' in data and osget and not osfim:
            # o.s did not finish and being initialized by user
            raise serializers.ValidationError(f"O.S j?? iniciada em {prochere}.")
           
        return data 

    def to_internal_value(self, data):   
        print(self.context['request'])
        url = self.context['request'].data['os']
        try:
            u = url.find('http')
            if  u < 0:
                token = url
            else:
                token = url[50:]  
       
            decodtoken = jwt.decode(token, peppertools.settings.SECRET_KEY ,algorithms=['HS256'])
            self.context['request'].data['os'] = decodtoken['osid']
        except:
            decodtoken = None
           
        print((decodtoken['osid'] if decodtoken and 'osid' in decodtoken else url))
        osid = decodtoken['osid'] if decodtoken  and 'osid' in decodtoken else url
        data['os'] = Cadastro_OS.objects.get(pk=osid) if Cadastro_OS.objects.filter(pk=osid).exists() else None
        print(data['os'])
        data['processo'] =  Processo.objects.get(pk=data['processo']) if Processo.objects.filter(pk=data['processo']).exists() else None
        print(data['processo'])
        return data

    class Meta:
        model = Historico_Os
        fields = ('processo', 'os', 'qtd' ,'ocorrencias', 'periodo','inicio', 'fim')
       
class Cadastro_OS_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cadastro_OS
        fields = ('STATUS', 'Prazo', 'Numero_Os', 'id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
class UserOsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    os = Cadastro_OS_Serializer(read_only=True)
    class Meta:
        model = Historico_Os
        fields = ('__all__')