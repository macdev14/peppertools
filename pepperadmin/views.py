from django.shortcuts import render, redirect
import jwt
import peppertools.settings

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

