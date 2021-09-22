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
        osedit = None
        osget = None
        edinicio, edfim, edproc = None, None, None

       
        try:
            allos = Historico_Os.objects.filter(os=data["os"])
            period = allos.aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(os=data["os"], periodo=period['periodo__max'])
        except Exception as e:
            print(e) 
       
        if osget:
            edfim = osget.fim
            edinicio = osget.inicio
            edproc = osget.processo
        # se finalizada mas iniciar novamente
        if edfim and 'inicio' in data and edinicio and edproc == data['processo']:
            # se estiver finalizado criar outro 
            print(f"periodos: {period}")
            data['periodo'] = period['periodo__max'] + 1
            periodoprint= data['periodo']
            hist_os = Historico_Os.objects.create(inicio=data['inicio'], periodo=data['periodo'], qtd=data['qtd'], os=data["os"], processo=data['processo'])
            return hist_os

        elif edinicio and 'fim' in data:
            Historico_Os.objects.filter(os=data["os"], periodo=period['periodo__max']).update(ocorrencias=data["ocorrencias"], fim=data["fim"] )
            hist_os =  Historico_Os.objects.get(os=data["os"], periodo=period['periodo__max'])
            return hist_os
        elif not edfim and 'inicio' in data:
           hist_os = Historico_Os.objects.create(inicio=data['inicio'], periodo=1, qtd=data['qtd'], os=data["os"], processo=data['processo'])
           return hist_os
        
    def validate(self, data):
        if not data['processo']:
            raise serializers.ValidationError("Processo não encontrado.")
        elif not data['os']:
            raise serializers.ValidationError("Ordem de Serviço não encontrada.")
            
        allos = Historico_Os.objects.filter(os=data["os"]).exists()
        osget, prochere, osinicio, osfim = None, None, None, None
        if allos:
            period = Historico_Os.objects.filter(os=data["os"]).aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(periodo=period['periodo__max'], os=data["os"])
            prochere = osget.processo
            #proc = Processo.objects.get(pk=osget.processo.id)
            osinicio = osget.inicio
            osfim = osget.fim
           
        if osget and 'fim' in data and not osget.inicio:
            # o.s exists but not ended
            raise serializers.ValidationError("O.S não iniciada.")
        
        elif osget and 'fim' in data and prochere.id != data['processo'].id:
            raise serializers.ValidationError(f"O.S iniciada em {prochere}.")

        elif 'fim' in data and osfim:
            raise serializers.ValidationError(f"O.S já finalizada em {prochere}.")
        elif 'fim' in data and not allos:
            # o.s does not exist and not initialized
            raise serializers.ValidationError("O.S não iniciada.")
        elif 'inicio' in data and osget and not osfim:
            # o.s did not finish and being initialized by user
            raise serializers.ValidationError(f"O.S já iniciada em {prochere}.")
           
        return data 

    def to_internal_value(self, data):   
        url = self.context['request'].data['os']
        u = url.find('http')
        if  u < 0:
            token = url
        else:
            token = url[50:]    
        try:
            decodtoken = jwt.decode(token, peppertools.settings.SECRET_KEY ,algorithms=['HS256'])
            self.context['request'].data['os'] = decodtoken['osid']
        except:
            decodtoken = None
        print(decodtoken['osid'])
        osid = decodtoken['osid'] if decodtoken else None
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
        fields = ('STATUS',)
