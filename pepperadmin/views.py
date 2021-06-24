from django.shortcuts import render, redirect
import jwt
import peppertools.settings
from easy_pdf.views import PDFTemplateView
# Create your views here.
def tokRedirect(request, token):
    try:
        tok = jwt.decode(token, peppertools.settings.SECRET_KEY, algorithms=['HS256'])
        osid = tok['osid']
        return redirect("admin:pepperadmin_cadastro_os_change", osid)
    except:
        return redirect("admin:index")

class HelloPDFView(PDFTemplateView):
    template_name = 'pepperadmin/Orcamento.html'
