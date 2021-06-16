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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from pepperadmin.views import tokRedirect
urlpatterns = i18n_patterns(
    # ...
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico") ) ),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index')) ),
    path('admin/os/change/<str:token>', tokRedirect, name="tokenRedirect"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # ...
 
    # If no prefix is given, use the default language
    prefix_default_language=False
)

#admin.site.site_header = 'Pimentel Ferramentas'