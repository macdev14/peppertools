from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

import peppertools.settings
from pysigep.client import SOAPClient
from pysigep.utils import URLS, HOMOLOGACAO, PRODUCAO
from .etiquetas_correios import *
from peppertools.settings import HOMOG_USUARIO, HOMOG_SENHA, HOMOG_CARTAO, HOMOG_CODIGO_ADMIN, HOMOG_CONTRATO, HOMOG_CNPJ

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