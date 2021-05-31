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
from django.shortcuts import render
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
        return render(request, 'pepperadmin/os.html',  {'field': obj,'qr':svg, 'tracker': historyos })   
         
    printos.label = 'Imprimir O.S'
    printos.short_description = 'Clique para imprimir ordem de serviço'
    change_actions = ('printos',)
    class Meta:
        verbose_name = _("Ordem de Serviço")

class ClienteModel(admin.ModelAdmin):
    list_display=('nome','cnpj','telefone')
    search_fields = ('nome', 'cnpj')
    


admin.site.register(Cliente, ClienteModel)
admin.site.register(Cadastro_OS, osModel)
admin.site.register(Item)
admin.site.register(Orcamento)
admin.site.register(Linha)
admin.site.register(Material)
admin.site.register(Historico_Os)
admin.site.register(Processo)
admin.site.disable_action('delete_selected')
