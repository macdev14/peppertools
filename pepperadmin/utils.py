from io import BytesIO, StringIO

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
from datetime import datetime
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
import base64





# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = context_dict
#     html  = template.render(context)
#     response = HttpResponse(content_type='application/pdf')

#     pdf = pisa.CreatePDF(html.encode("ISO-8859-1"), dest=response)
#     if not pdf.err:
#         return HttpResponse(content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
#     #pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     #return response










