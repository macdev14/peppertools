from django.shortcuts import render, redirect
import jwt
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth import authenticate
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

    

# def register(request):
#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('register')

#     else:
#         f = UserCreationForm()

#     return render(request, 'admin/register.html', {'form': f})


def register_view(request):
    
    if  request.method == 'POST':
        
        try:
            userform = UserForm(request.POST)
            errors = userform.errors.as_json()
            errors = json.loads(errors)
            for message in errors:
               messages.add_message(request, messages.INFO, message + ': '+ errors[message][0]['message'])
            if not errors:
                try:
                    user = User.objects.create_user(email=userform['email'].data, password=userform['password'].data)
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError as e:
                    messages.add_message(request, messages.INFO, 'Conta já existente.')
                
        except Exception as e:
            print(e)
            messages.add_message(request, messages.INFO, 'Erro ao cadastrar.')
            pass
        

    userform = UserForm(request.POST or None)
    return render(request, "register.html", { 'userform': userform })




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["email"]
        password = request.POST["password"]
      
        user = authenticate(request, username=username, password=password)
        

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("userlogin")
        else:
            messages.add_message(request, messages.INFO, 'Senha e/ou email inválido.')

    
    return render(request, "user_login.html")
    
   