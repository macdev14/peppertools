"""peppertools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
import django.http
from django.urls import path, include
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from pepperadmin.models import Historico_Os, Processo
from pepperadmin.views import tokRedirect
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.views.generic.list import ListView
from controlcenter.views import controlcenter

def ssl_view(request):

    content = '3ntwQiXqiZ77EFQlJtaWlZzmkA_zu8lkhXWpCzv0nmI.1tWBfLlnFRvAzp8SnlPF8GQsqCxzC36BC1vRDGe0sFs'
    return HttpResponse(content, content_type='text/plain')



class ListProcessesView(ListView):
    model = Historico_Os

    def get_queryset(self, *args, **kwargs): 
        qs = super().get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
       
        return qs

   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        processes = Processo.objects.all()
        rows = {}
        for process in processes:
            os_queryset = Historico_Os.objects.filter(processo=process).order_by('-data')
            os_string_list = [str(obj.os.Numero_Os) + ' ' + str(obj.data.strftime("%d/%m/%Y" )) for obj in os_queryset]
            os_string = '   <br> <br> '.join(os_string_list)
            rows[process.procname] = os_string
        # for entry in historico_entries:
        #     procname = entry.processo.procname
        #     if procname not in historico_by_process:
        #         historico_by_process[procname] = []
        #     historico_by_process[procname].append(entry)
        context['historico_by_process'] = rows
        context['processes'] = processes

        return context


# path('', RedirectView.as_view(url=reverse_lazy('admin:index')) ),
urlpatterns = i18n_patterns(
    # ...
    path('admin/process/', ListProcessesView.as_view(template_name='admin/process/process.html'), name='process-table'),
    #path("process/", include('pepperadmin.urls') ),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico") ) ),
    path('', lambda request: redirect('admin/', permanent=True) ),
    path('admin/os/change/<str:token>', tokRedirect, name="tokenRedirect"),
    path('admin/dashboard/', controlcenter.urls),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('.well-known/acme-challenge/3ntwQiXqiZ77EFQlJtaWlZzmkA_zu8lkhXWpCzv0nmI', ssl_view),
    
    # ...
 
    # If no prefix is given, use the default language
    prefix_default_language=False
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#admin.site.site_header = 'Pimentel Ferramentas'