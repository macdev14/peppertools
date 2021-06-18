from pepperadmin.models import *
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt
import peppertools.settings
from django.db.models import Max
'''
from rest_framework_jwt.settings import api_settings



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
'''

class ProcessoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processo
        fields = ('id', 'procname','Tempo_Objetivo',)



class HistoricoSerializer(serializers.ModelSerializer):
    #ostok = serializers.SerializerMethodField(read_only=True)
    
    def create(self, data):
        osedit = None
        osget = None
        try:
            allos = Historico_Os.objects.filter(os=data["os"])
            period = allos.aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(periodo=period['periodo__max'])
        except:
            pass 
           
        print("teste::")
        
        try:
            edfim = osget.fim
            edinicio = osget.inicio
            edproc = osget.processo
        except:
            edfim = None
            edinicio = None
        
            
        if edfim and 'inicio' in data:
            # se estiver finalizado criar outro
            
            print(f"periodos: {period}")
            data['periodo'] = period['periodo__max'] + 1
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
      
        allos = Historico_Os.objects.filter(os=data["os"]).exists()
        if allos:
            period = Historico_Os.objects.filter(os=data["os"]).aggregate(Max('periodo'))
            osget = Historico_Os.objects.get(periodo=period['periodo__max'])
            prochere = osget.processo
            #proc = Processo.objects.get(pk=osget.processo.id)
            osinicio = osget.inicio
            osfim = osget.fim

        if osget and 'fim' in data and not osinicio:
            # o.s exists but not ended
            raise serializers.ValidationError("O.S não iniciada.")
        
        elif osget and 'fim' and prochere.id != data['processo'].id:
            raise serializers.ValidationError(f"O.S iniciada em {prochere}.")

        elif 'fim' in data and osfim:
            raise serializers.ValidationError(f"O.S já finalizada em {prochere}.")
        elif 'fim' in data and not allos:
            # o.s does not exist and not initialized
            raise serializers.ValidationError("O.S não iniciada.")
        elif 'inicio' in data and not osfim:
            # o.s did not finish and being initialized by user
            raise serializers.ValidationError(f"O.S já iniciada em {prochere}.")
        
        
        return data 



    def to_internal_value(self, data):
        print('initial:')
        print(data)
        url = self.context['request'].data['os']
       
        print("test: ")
        print(url)
        u = url.find('http')
        print(u)
        if  u < 0:
            print('test')
            print(url)
            token = url
        else:
            token = url[50:]
        print('token2:')
        print(token)
        print(f"processo: {data['processo']}")
        decodtoken = jwt.decode(token, peppertools.settings.SECRET_KEY ,algorithms=['HS256'])
        self.context['request'].data['os'] = decodtoken['osid']
        data['os'] = decodtoken['osid']
        proc = Processo.objects.get(pk=int(data['processo']))
        osinstance = Cadastro_OS.objects.get(pk=data['os'])
       


        data['os'] = osinstance
        data['processo'] = proc
        print('final:')
        print(data)
        return data
    '''
    def validate(self, obj):
        url = self.context['request'].data['os']
       
        print("test: ")
        print(url)
        u = url.find('http')
        print(u)
        if  u < 0:
            print('test')
            print(url)
            token = url
        else:
            pass
            #token = url[49:]
        print('token2:')
        print(token)
        decodtoken = jwt.decode(token, peppertools.settings.SECRET_KEY ,algorithms=['HS256'])
        self.context['request'].data['os'] = decodtoken['osid']
    
   
    
    def get_ostok(self, obj):
        #print(self.context['request'].data['id_os'])
        try:
            url = self.context['request'].data['ostok']
            url = url['os']
            print("test: ")
            print(url)
            #print(self.context['request'].data['id_os'])
            
            token = url
            print('token2:')
            print(token)
            decodtoken = jwt.decode(token, peppertools.settings.SECRET_KEY ,algorithms=['HS256'])
            print('tktest:')
            print(decodtoken['osid'])
            #self.context['request'].data['os'] = decodtoken['osid']
            print('request modified:')
            #print(self.context['request'].data['os'])
            obj.os_id = decodtoken['osid']
            return decodtoken['osid']
            #self.context['request'].data['id_os'] = decodtoken['osid']
        except:
            pass
    '''
    class Meta:
        model = Historico_Os
        fields = ('processo', 'os', 'qtd' ,'ocorrencias', 'periodo','inicio', 'fim')
       

    
class Cadastro_OS_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cadastro_OS
        fields = ('STATUS',)
    
'''
class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
          
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username':username,
            'token': jwt_token
        }
'''