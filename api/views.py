from django.shortcuts import render
from pepperadmin.models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsOwnerProfileOrReadOnly
import datetime as datetime2
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
        funcid = self.request.GET['id_func'] if 'id_func' in self.request.GET else self.request.user.id
        
        if funcid and Historico_Os.objects.filter(colaborador=funcid).exists():
            try:
                active_on = datetime2.date(timezone.now().year, timezone.now().month, timezone.now().day-3)
            except:
                active_on = datetime2.date(timezone.now().year-1, 12, 31)
            
            next_day = datetime2.date(timezone.now().year, timezone.now().month, timezone.now().day+7)
            print(active_on)
            print(next_day)
            #print(Historico_Os.objects.filter(colaborador=funcid, data__range=(datetime2.date(datetime2.datetime.now().year-1, 12, 31),  )).exists() )
            return Historico_Os.objects.filter(colaborador=funcid, data__range=(active_on, next_day ))
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