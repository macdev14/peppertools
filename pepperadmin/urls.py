from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('userregister', views.register_view, name='userregister'),
    # ex: /polls/5/
    path('userlogin', views.login_view, name='userlogin'),
    # ex: /polls/5/results/
   
]