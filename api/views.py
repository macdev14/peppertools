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
    print(queryset)
    serializer_class = ProcessoSerializer


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