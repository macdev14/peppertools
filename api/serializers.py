from pepperadmin.models import *
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt
'''
from rest_framework_jwt.settings import api_settings



JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
'''

class ProcessoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processo
        fields = ('procname','Tempo_Objetivo',)



class HistoricoSerializer(serializers.ModelSerializer):
    ostok = serializers.SerializerMethodField(read_only=True)
    def get_ostok(self, obj):
        print(self.context['request'].data['os'])
        try:
            url = self.context['request'].data['os']
            if 'http' in url:
                token = url[49:]
            else:
                token = url
            decodtoken = jwt.decode(token, algorithms=['HS256'])
            self.context['request'].data['os'] = decodtoken['os']
            print(self.context['request'].data['os'])
        except:
            pass
    class Meta:
        model = Historico_Os
        fields = ('id_proc', 'os', 'qtd' ,'ocorrencias', 'ostok')
       

    
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