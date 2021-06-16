from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.views import(
    obtain_auth_token
)
router = routers.DefaultRouter()
router.register(r'processos', views.ProcViewSet)
router.register(r'historico_os', views.HistoricalView)
router.register(r'ordem_de_servico', views.Cadastro_OSView)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

class OSserializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        print(user.password)

        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = OSserializer

urlpatterns = [
    path('app/api/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]