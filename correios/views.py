from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

from pysigep.client import SOAPClient
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO
from etiquetas_correios import *

HOMOG_CODIGO_ADMIN = '12517429'
HOMOG_USUARIO  = 'papper2016**'
HOMOG_SENHA = 'xdo3fn'
HOMOG_CARTAO = '0065585534'
HOMOG_CONTRATO = '9912314545'
HOMOG_CNPJ='05.499.375/0001-61'

'''
SENHA_2 = '05499375'
HOMOG_USUARIO = 'sigep'
HOMOG_SENHA = 'n5f9t8'
HOMOG_CARTAO = '0067599079'
HOMOG_CODIGO_ADMIN = '17000190'
HOMOG_CONTRATO = '9992157880'
HOMOG_CNPJ = '38.875.380/0001-80'
'''
class CorreiosListView(TemplateView):
    template_name = 'correios/correios_list.html'

    

    def get_context_data(self, **kwargs):
        params = {
        'cod_administrativo': HOMOG_CODIGO_ADMIN,
        'numero_servico': '04162',
        'cep_origem': '70002900',
        'cep_destino': '70.002-900',
        }


    
   
        cliente = SOAPClient(ambiente=PRODUCAO,  usuario=HOMOG_USUARIO, senha=HOMOG_SENHA)
        disponibilidade = cliente.verifica_disponibilidade_servico(**params)
        print('disponivel: ')
        print(True if disponibilidade else False)
    
    
        params2 = {
            'numero_cartao_postagem': HOMOG_CARTAO,
        }

        status = cliente.get_status_cartao_postagem(**params2)

        print(status)

        endereco = cliente.consulta_cep('12900300')
        print(endereco)
        context = super(CorreiosListView, self).get_context_data(**kwargs)
        context['postagens'] = endereco
        return context



class CorreiosTagView(TemplateView):
    template_name = 'correios/declaracao_conteudo.html'

   
    

    def get_context_data(self, **kwargs):
        params = {
        'cod_administrativo': HOMOG_CODIGO_ADMIN,
        'numero_servico': '04162',
        'cep_origem': '70002900',
        'cep_destino': '70.002-900',
        }


        print(self.request)    
   
        cliente = SOAPClient(ambiente=PRODUCAO,  usuario=HOMOG_USUARIO, senha=HOMOG_SENHA)
        disponibilidade = cliente.verifica_disponibilidade_servico(**params)
        print('disponivel: ')
        print(True if disponibilidade else False)
    
    
        params2 = {
            'numero_cartao_postagem': HOMOG_CARTAO,
        }

        status = cliente.get_status_cartao_postagem(**params2)

        print(status)

        endereco = cliente.consulta_cep('12900300')
        print(endereco)
        context = super(CorreiosTagView, self).get_context_data(**kwargs)
        context['postagens'] = endereco
        return context