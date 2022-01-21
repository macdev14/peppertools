from django.shortcuts import render, redirect
import jwt
from django import forms
import peppertools.settings
from django.contrib.auth.forms import UserCreationForm
from .models import *
# Create your views here.
def tokRedirect(request, token):
    if not request.is_secure() and  peppertools.settings.DEBUG == False:
        peppertools.settings.SECURE_SSL_REDIRECT = True
    try:
        tok = jwt.decode(token, peppertools.settings.SECRET_KEY, algorithms=['HS256'])
        osid = tok['osid']
        return redirect("admin:pepperadmin_cadastro_os_change", osid)
    except:
        return redirect("admin:index")

class UserForm(forms.ModelForm):
    # fields = [
    #     "name",
    #     "email",
    #     "identity",
    #     "pis",
    #     "country",
    #     "state",
    #     "city",
    #     'street',
    #     "number"
    # ]
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = User
        fields = '__all__'

    

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'cadmin/register.html', {'form': f})