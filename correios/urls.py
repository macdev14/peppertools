from django.urls import path

from .views import CorreiosListView, CorreiosTagView

urlpatterns = [
    path('', CorreiosListView.as_view(), name='correios-list'),
    path('tag/<int:number>', CorreiosTagView.as_view(), name='correios-tag')
]
