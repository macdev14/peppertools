from django.contrib import admin
from peppertools.settings import SECRET_KEY
from .models import *
from django.utils.translation import ugettext_lazy as _
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
import peppertools.settings
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.shortcuts import render, redirect
from datetime import datetime
#from .utils import render_to_pdf
from simple_history import admin as simpleHistory
import jwt
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from easy_pdf.rendering import render_to_pdf
from django.db.models import Max, F
class renderOS(PDFTemplateView, PDFTemplateResponseMixin):
    model = Cadastro_OS
    template_name = 'pepperadmin/os.html'
    encoding = "utf-8",

class osModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    list_display=('Numero_Os','Cliente','Tipo','Quantidade')
    search_fields = ('Numero_Os', 'Especificacao' )
    readonly_fields=('Data',)
    def printos(self, request, obj):
        
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
                    ocortimeproc.append(processo + ': ' + ocorrencia)
            historyos = ocortimeproc
            processes = allprocdesc
            #print(processos_dis)
            #print(allocorrencias)
            #print(allprocdesc)
        #processes = Processo.objects.all()
        return render(request, 'pepperadmin/os.html',  {'field': obj,'qr':svg, 'historyos': historyos, 'processes':processes })   
         
    printos.label = 'Imprimir O.S'
    printos.short_description = 'Clique para imprimir ordem de serviço'
    change_actions = ('printos',)
    class Meta:
        verbose_name = _("Ordem de Serviço")

class ClienteModel(simpleHistory.SimpleHistoryAdmin):
    list_display=('nome','cnpj','telefone')
    search_fields = ('nome', 'cnpj')
    
class OrcamentoModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    filter_horizontal = ("item",)
    def createPedido(self, request,obj):
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
    createPedido.label = 'Criar Pedido'
    createPedido.short_description = 'Clique aqui para criar pedido do orçamento.'
    change_actions = ('createPedido',)

class PedidoModel(DjangoObjectActions, simpleHistory.SimpleHistoryAdmin):
    filter_horizontal = ("item",)
    def createOs(self, request, obj):
        if obj.os_pedido:
            os = Cadastro_OS.objects.get(pk=obj.os_pedido.id)
            if os:
               return redirect("admin:pepperadmin_cadastro_os_change", obj.os_pedido.id)
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
        orc = Orcamento.objects.get(pedido_id=obj.id)
        prazo = orc.prazo_entrega
        os = Cadastro_OS.objects.create(Cliente=obj.Cliente, Especificacao=obj.Especificacao, Desenho_Pimentel=obj.desenho, Material=materialadd, Ferramenta = ferramenta, Numero_Pedido=obj.numero_pedido, Prazo = prazo, Data_Pedido=obj.data_entrada or None, Quantidade=qtd, unidade=obj.unidade_pedido) 
        os.save()
        Pedido.objects.filter(pk=obj.id).update(os_pedido=os.id)
        return redirect("admin:pepperadmin_cadastro_os_change", os.id)
    createOs.label = "Criar O.S"
    createOs.short_description = 'Clique aqui para criar uma ordem de serviço do pedido.'
    change_actions = ('createOs',)


admin.site.register(Cliente, ClienteModel)
admin.site.register(Cadastro_OS, osModel)
admin.site.register(Item, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Orcamento, OrcamentoModel)
admin.site.register(Linha, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Material, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Historico_Os, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Processo, simpleHistory.SimpleHistoryAdmin)
admin.site.register(Pedido, PedidoModel)
admin.site.register(Ferramenta, simpleHistory.SimpleHistoryAdmin)
