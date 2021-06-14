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
#from .utils import render_to_pdf
import jwt
from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin
from easy_pdf.rendering import render_to_pdf

class renderOS(PDFTemplateView, PDFTemplateResponseMixin):
    model = Cadastro_OS
    template_name = 'pepperadmin/os.html'
    encoding = "utf-8",

class osModel(DjangoObjectActions, admin.ModelAdmin):
    list_display=('Numero_Os','Cliente','Tipo','Quantidade')
    search_fields = ('Numero_Os', 'Especificacao' )
    readonly_fields=('Data',)
    def printos(self, request, obj):
        
        codyear = str(obj.Data.year)
        obj.Data_digit = codyear[-2:]
        osid = obj.id
        qr = jwt.encode({'osid': osid }, peppertools.settings.SECRET_KEY)
        print(qr)
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(qr, image_factory=factory, box_size=7)
        stream = BytesIO()
        img.save(stream)
        svg = stream.getvalue().decode()
        historyos = Historico_Os.objects.all().filter(os=obj.id)
        processes = Processo.objects.all()
        return render(request, 'pepperadmin/os.html',  {'field': obj,'qr':svg, 'tracker': historyos, 'processes':processes })   
         
    printos.label = 'Imprimir O.S'
    printos.short_description = 'Clique para imprimir ordem de serviço'
    change_actions = ('printos',)
    class Meta:
        verbose_name = _("Ordem de Serviço")

class ClienteModel(admin.ModelAdmin):
    list_display=('nome','cnpj','telefone')
    search_fields = ('nome', 'cnpj')
    
class OrcamentoModel(DjangoObjectActions, admin.ModelAdmin):
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

class PedidoModel(DjangoObjectActions, admin.ModelAdmin):
    filter_horizontal = ("item",)
    def createOs(self, request, obj):
        if obj.os_pedido:
            os = Cadastro_OS.objects.get(pk=obj.os_pedido.id)
            if os:
               return redirect("admin:pepperadmin_cadastro_os_change", obj.os_pedido.id)
        materialadd = ''
        qtd = 0
        precototal = 0
        for item in obj.item.all():
            print(item)
            materialadd = materialadd  + ' '+ item.nome
            qtd = qtd + item.qtd
            precototal = precototal + item.preco
        print(materialadd)
        os = Cadastro_OS.create(Cliente=obj.Cliente, Especificacao=obj.especificacao, desenho_pimentel=obj.desenho, Material=materialadd, gravacao=obj.gravacao, numero_pedido=obj.numero_pedido, data_pedido=obj.data_entrada, Quantidade=qtd) 
        os.save()
        Pedido.objects.filter(pk=obj.numero_pedido).update(os_pedido=os.id)
        return redirect("admin:pepperadmin_cadastro_os_change", os.id)
    createOs.label = "Criar O.S"
    createOs.short_description = 'Clique aqui para criar uma ordem de serviço do pedido.'
    change_actions = ('createOs',)


admin.site.register(Cliente, ClienteModel)
admin.site.register(Cadastro_OS, osModel)
admin.site.register(Item)
admin.site.register(Orcamento, OrcamentoModel)
admin.site.register(Linha)
admin.site.register(Material)
admin.site.register(Historico_Os)
admin.site.register(Processo)
admin.site.register(Pedido, PedidoModel)
admin.site.register(Ferramenta)
