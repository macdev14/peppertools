from django.urls import reverse
from django.test import Client, override_settings, TestCase
from .models import *
# Create your tests here.
@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class SystemTests(TestCase):
    def setUp(self):
       
        
       
        # Create superuser
        self.user = User.objects.create_superuser(
        username='new_user', email='test@example.com', password='password',
        )
        # Set server client
        self.client = Client()
        # Log in
        self.client.login(username='new_user', password='password')
        # Create Customer Object 
        self.customer = Cliente.objects.create(id=1, nome="teste")
        # Create service order
        self.service_order = Cadastro_OS.objects.create(Cliente=self.customer, Numero_Os=1)

        self.processo = Processo.objects.create(procname="corte")
        
        self.formato = Formato.objects.create(nome="DIN371")
        # Create item
        self.item = Ferramenta.objects.create(nome="Test")
        self.item.processos.set(Processo.objects.filter(pk=self.processo.id))
        self.item.save()
        # Create quote
        
       
        self.quote = Orcamento.objects.create(cliente=self.customer, numero=1)
        self.quote = Orcamento.objects.get(pk=self.quote.id)
        self.quote.ferramenta.set(Ferramenta.objects.filter(pk=self.item.id))
        self.quote.save()
        
    def test_print_os(self): 
        ''' Imprimir O.S '''
        change_url = reverse('admin:pepperadmin_cadastro_os_changelist')
        response = self.client.post(change_url, {'action': 'printos', '_selected_action': self.service_order.id })
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    SystemTests.main()