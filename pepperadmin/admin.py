from django.contrib import admin
from peppertools.settings import SECRET_KEY
from .models import *
from django.utils.translation import ugettext_lazy as _
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
import peppertools.settings
import qrcode
import qrcode.image.svg
from django.db.models.query import QuerySet
from io import BytesIO
from django.shortcuts import render, redirect
from datetime import datetime
import datetime as datetime2
from django.contrib import messages
from .utils import render_to_pdf as render_pdf
from simple_history import admin as simpleHistory
import jwt
from tabular_export.admin import export_to_csv_action, export_to_excel_action

from django.db.models import Max, F


class osModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    
    def status_time(self, obj):
        
      
        if Historico_Os.objects.filter(os_id=obj.id).exists():
            os = Historico_Os.objects.filter(os_id=obj.id)
            time_total = datetime2.timedelta()
            for time in os:
               if not time.fim: break
               enter_delta = datetime2.timedelta(hours=time.inicio.hour, minutes=time.inicio.minute, seconds=time.inicio.second)
               exit_delta = datetime2.timedelta(hours=time.fim.hour, minutes=time.fim.minute, seconds=time.fim.second)
               difference_delta = exit_delta - enter_delta

               time_total +=difference_delta
               #time_total_out = time_total
            return time_total
        else:
            return "Não iniciada"
    status_time.short_description = 'Tempo total'
    list_display=('Numero_Os','Cliente','Tipo', 'Numero_Nf','Quantidade', 'STATUS', 'status_time')
  
    search_fields = ('Numero_Os', 'Especificacao', 'Cliente__nome', 'Numero_Nf', 'STATUS', 'Quantidade' )
    readonly_fields=('Data',)
    def printos(self, request, obj):
       
        if isinstance(obj, QuerySet):
            obj = obj.first()
        codyear = str(obj.Data.year)
        obj.Data_digit = codyear[-2:]
        osid = obj.id
        qr = 'https://peppertools.herokuapp.com/admin/os/change/' + jwt.encode({'osid': osid }, peppertools.settings.SECRET_KEY)
        #print(qr)
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(qr, image_factory=factory, box_size=5)
        stream = BytesIO()
        img.save(stream)
        svg = stream.getvalue().decode()
        historyos = Historico_Os.objects.filter(os=obj.id).exists()
        processes = None
        if historyos:
            # max period
            teste = Historico_Os.objects.filter(os=obj.id).aggregate(latest=Max('periodo'))
            all_proc = Historico_Os.objects.filter(os=obj.id).values_list('processo__procname','processo' ,'periodo','ocorrencias')
            processos_dis = list(dict.fromkeys(all_proc))
            #print(all_proc)
            allprocdesc = []
            ocortimeproc = []
            #allocorrencias = []
            #ocor = Historico_Os.objects.filter(os=obj.id).only('ocorrencias')
            #allocorrencias.append({ procins.procname : ocor } ) 
            for processo, proc_id, periodo, ocorrencia in processos_dis:
                procins = Processo.objects.get(pk=proc_id)
                lateperiod = Historico_Os.objects.filter(os=obj.id, processo=procins).aggregate(latest=Max('periodo'))
                procview = Historico_Os.objects.get(os=obj.id, processo=procins, periodo=lateperiod['latest'])
                if procview not in allprocdesc:
                   allprocdesc.append(procview)
                if ocorrencia:
                    print(any(processo in word  for word in ocortimeproc))
                    if not any(processo in word for word in ocortimeproc):
                        
                        ocortimeproc.append(processo.upper() + ': ' + ocorrencia.rstrip())
                    else:
                        index = None
                        for ocor in ocortimeproc:
                            if processo in ocor:
                                index = ocortimeproc.index(ocor)
                        #print(index)
                        #lenstr = len(ocortimeproc[index]) - 1
                        '''
                        if ocortimeproc[index][lenstr-1:] == ' ':
                            print(ocortimeproc[index][lenstr-1:])
                            ocortimeproc[index] = ocortimeproc[index][:lenstr-1]
                        '''
                        ocortimeproc[index] = ocortimeproc[index] + ', ' + ocorrencia.rstrip()
            historyos = ocortimeproc
            processes = allprocdesc
            #print(processos_dis)
            #print(allocorrencias)
            #print(allprocdesc)
        #processes = Processo.objects.all()
        return render(request, 'pepperadmin/os.html',  {'field': obj,'qr':svg, 'historyos': historyos, 'processes':processes })   
         
    printos.label = 'Imprimir O.S'
    printos.short_description = 'Imprimir ordem de serviço'
    change_actions = ('printos',)
    actions = ['printos']
    class Meta:
        verbose_name = _("Ordem de Serviço")

class ClienteModel(simpleHistory.SimpleHistoryAdmin):
    list_display=('nome','cnpj','telefone')
    search_fields = ('nome', 'cnpj')
    
class OrcamentoModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    def printOrcamento(self, request, obj):
        

        total=0
        for item in obj.item.all():
            if type(item.preco) is not float or type(item.qtd) is not float:
                messages.add_message(request, messages.WARNING, 'Preço ou Quantidade inválida.')
                print(item.id)
                return redirect("admin:pepperadmin_ferramenta_change", item.id)
            subtotal = (item.preco * item.qtd)
            total = subtotal + total
            
        return render(request, 'pepperadmin/Orcamento.html',  {'orcamento': obj, 'total':total })
       

            
    printOrcamento.label = 'Imprimir Orçamento'
    printOrcamento.short_description = 'Imprimir Orçamento'
    


    def createselected(self, obj):
        
        if obj.pedido_id != None:
            ped = Pedido.objects.get(pk=obj.pedido_id.id)
            if ped:
                return #redirect("admin:pepperadmin_pedido_change", obj.pedido_id.id)
        
            
        price = 0
        for i in obj.item.all():
            print(i)
            price = price + i.preco
                
        pedido = Pedido(Cliente=obj.cliente,qnt = obj.qnt,preco_pedido=price)
        pedido.save()
        Orcamento.objects.filter(pk=obj.numero).update(pedido_id=pedido.id)
            
        for content in obj.item.all():
            pedido.item.add(content)
            print(pedido.item)
            pedido.save()
                

        print(pedido.id)
        return #redirect("admin:pepperadmin_pedido_change", pedido.id)
    
    filter_horizontal = ("item",)
    
    def createPedido(self, request,obj):
        
        try:
            if isinstance(obj, QuerySet):
                for object in obj:
                    self.createselected(object)
                return messages.add_message(request, messages.SUCCESS, 'Pedido(s) criados.')
            
            if obj.pedido_id != None:
                ped = Pedido.objects.get(pk=obj.pedido_id.id)
                if ped:
                    return redirect("admin:pepperadmin_pedido_change", obj.pedido_id.id)
            price = 0
            for i in obj.item.all():
                print(i)
                price = price + i.preco
                
            pedido = Pedido(Cliente=obj.cliente,qnt = obj.qnt,preco_pedido=price)
            pedido.save()
            Orcamento.objects.filter(pk=obj.numero).update(pedido_id=pedido.id)
            
            for content in obj.item.all():
                pedido.item.add(content)
                print(pedido.item)
                pedido.save()
                

            print(pedido.id)
            return redirect("admin:pepperadmin_pedido_change", pedido.id)
        
        except Exception as e:
            print(e)

                    


                
    createPedido.label = 'Criar Pedido'
    createPedido.short_description = 'Criar pedido do orçamento.'
    change_actions = ('createPedido','printOrcamento')
    actions = ['createPedido', 'printOrcamento']
class PedidoModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    filter_horizontal = ("item",)
    def createOs(self, request=None, obj=None, list=None):
        if isinstance(obj, QuerySet) and not list:
            for object in obj:
                self.createOs(request=request,obj=object, list=True)
            return messages.add_message(request, messages.SUCCESS, 'Ordem de serviços(s) criados.')
        if obj.os_pedido and Cadastro_OS.objects.filter(pk=obj.os_pedido.id).exists():
            os = Cadastro_OS.objects.get(pk=obj.os_pedido.id)
            if os and not list:
               return redirect("admin:pepperadmin_cadastro_os_change", obj.os_pedido.id)
            return
        materialadd = ''
        qtd = 0
        precototal = 0
        ferramenta = ''
        for item in obj.item.all():
            #print(item)
            #print(item.material.all())
            #material_item = Item.objects.get(pk=item.id).only('material')
            #print(material_item)
            
            for material in item.material.all():
                print('material name: ')
                print(material.nome)
                materialadd = materialadd  + ' '+ material.nome
            ferramenta = ferramenta  + ' '+ item.nome
            qtd = qtd + item.qtd
            precototal = precototal + item.preco

        #return redirect("/")
        print(obj.id)
        prazo=None
        if  Orcamento.objects.filter(pedido_id=obj.id).exists():
            orc = Orcamento.objects.get(pedido_id=obj.id)
            prazo = orc.prazo_entrega
        os = Cadastro_OS.objects.create(Cliente=obj.Cliente, Especificacao=obj.Especificacao, Desenho_Pimentel=obj.desenho, Material=materialadd, Ferramenta = ferramenta, Numero_Pedido=obj.numero_pedido, Prazo = prazo or None, Data_Pedido=obj.data_entrada or None, Quantidade=qtd, unidade=obj.unidade_pedido) 
        os.save()
        if Pedido.objects.filter(pk=obj.id).exists():
            Pedido.objects.filter(pk=obj.id).update(os_pedido=os.id)
        if not list:
            return redirect("admin:pepperadmin_cadastro_os_change", os.id)
        return
    createOs.label = "Criar O.S"
    createOs.short_description = 'Criar ordem de serviço do pedido.'
    change_actions = ('createOs',)
    actions = ['createOs']


class FerramentaModel(simpleHistory.SimpleHistoryAdmin):
    filter_horizontal = ("processos", "material")
    def get_form(self, request, obj=None, **kwargs):
        users_in_group=None
        if Group.objects.filter(name="Producao").exists():
            users_in_group = Group.objects.get(name="Producao").user_set.all()
        if users_in_group:
            if request.user in users_in_group:
                self.fields = ('nome', 'material', 'arquivo_desenho', 'relatorio', 'descricao', 'passo', 'rosca', 'diamrosca', 'tolerancia')
        form = super().get_form(request, obj, **kwargs)
        return form

class Historico_OsAdmin(simpleHistory.SimpleHistoryAdmin):
    
    
    raw_id_fields=('os',)

    def time(self, obj):
        try:
            enter_delta = datetime2.timedelta(hours=obj.inicio.hour, minutes=obj.inicio.minute, seconds=obj.inicio.second)
            exit_delta = datetime2.timedelta(hours=obj.fim.hour, minutes=obj.fim.minute, seconds=obj.fim.second)
            difference_delta = exit_delta - enter_delta
            return difference_delta
        except:
            return 'Não Finalizado'
    def avg_qtd(self,obj):
        try:
            result_hour, plural_hour= None, None
            result =  self.time(obj).total_seconds()/obj.qtd/60
            plural = 'minutos' if round(result, 2) > 1 else 'minuto'
            if round(result, 2) >= 60:
                result_hour = round(round(result, 2)/60,2) 
                plural_hour = 'hora(s)'
                plural = plural+' / '
            return f'{round(result, 2)} {plural} {result_hour or ""} {plural_hour or ""}'
        except:
            return 'Não Finalizado'
    def date_obj(self,obj):
        try:
            return f'{obj.data.day}/{obj.data.month}/{obj.data.year}'
        except:
            return 'Data não encontrada.'
    avg_qtd.short_description = 'Tempo médio por peça'
    date_obj.short_description = 'Data'
    time.short_description = 'Tempo total'
    list_display=('os','qtd','processo','date_obj', 'time' , 'avg_qtd', 'inicio', 'fim', 'periodo')
    search_fields = ('processo__procname', 'qtd', 'os__Numero_Os', 'os__Cliente__nome', 'os__Numero_Nf' )
    actions = (export_to_csv_action, )


admin.site.register(Cliente, ClienteModel)
admin.site.register(Cadastro_OS, osModel)
admin.site.register(Item, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Orcamento, OrcamentoModel)
admin.site.register(Linha, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Material, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Historico_Os, Historico_OsAdmin)
admin.site.register(Processo, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Pedido, PedidoModel)
admin.site.register(Ferramenta, FerramentaModel)
admin.site.register(Rosca, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Formato, simpleHistory.SimpleHistoryAdmin)