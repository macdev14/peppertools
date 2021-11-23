from django.shortcuts import render
from django.shortcuts import render, redirect
from pepperadmin.models import *
from django import forms
# Create your views here.



def index(request):
    items = Item.objects.all()
    return render(request, "commerce/index.html", { 'items': items })