from django.shortcuts import render
from pepperadmin.models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsOwnerProfileOrReadOnly

# Create your views here.

class ProcViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Processo.objects.all().order_by('procname')
    serializer_class = ProcessoSerializer


class HistOsUserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserOsSerializer
    #queryset = Historico_Os.objects.all().order_by('id')
    def get_queryset(self):
        print(self.request.GET)
        funcid = self.request.GET['id_func'] if 'id_func' in self.request.GET else None
        if funcid and Historico_Os.objects.filter(colaborador=funcid).exists():
            return Historico_Os.objects.filter(colaborador=funcid)
        return Historico_Os.objects.all() 
    #def get(self, request, **kwargs):
        

class HistoricalView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Historico_Os.objects.all().order_by('id')
    serializer_class = HistoricoSerializer
    
    


class Cadastro_OSView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cadastro_OS.objects.all().order_by('Numero_Os')
    serializer_class = Cadastro_OS_Serializer
class LongLoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)