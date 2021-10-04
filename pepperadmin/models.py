from django.db import models
from localflavor.br.models import BRCPFField, BRCNPJField, BRPostalCodeField, BRStateField
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
#from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
#from .utils import get_last_periodo
# Create your models here.
from simple_history.models import HistoricalRecords
from django.utils import timezone
from django.core.exceptions import  ObjectDoesNotExist
from django.contrib.auth.models import User, Group

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import signals
from django.contrib.auth.signals import user_logged_in
#signal used for is_active=False to is_active=True

@receiver(pre_save, sender=User, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active and User.objects.filter(pk=instance.pk, is_active=True).exists():
        subject = 'Active account'
        message = '%s your account is now active' %(instance.username)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)


def login_handler(sender, user, request, **kwargs):
    print('logged in')
    subject = f'{user.username} realizou login'
    message = f'{user.username} realizou login'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)


user_logged_in.connect(login_handler)

osid = None




def get_last_os():
    largest = Cadastro_OS.objects.values("Numero_Os").latest('Numero_Os')
    print(largest['Numero_Os'])
    if not largest:
        return 1
    return largest['Numero_Os'] + 1




def get_last_periodo(osid):
    lastperiodo = Historico_Os.objects.values('periodo').filter(os=osid).latest('periodo')
    #print(lastperiodo['periodo'])
    if not lastperiodo:
        return 1
    return lastperiodo['periodo'] + 1

def get_last_pedido():
    
    if Pedido.objects.exists():
        return 2
    return 1
    
   
       
   
        


def current_year():
    return datetime.now().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

def year_choices():
    return [(r,r) for r in range(1984, datetime.now().year+1)]


def set_periodo(osid):
    return get_last_periodo(osid)



class Processo(models.Model):
    procname = models.CharField(_("Nome"), null=True, blank=True,max_length=254, db_column='Nome')
    Tempo_Objetivo = models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False, db_column='Tempo_Objetivo')
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.procname}"
    class Meta:
        db_table = 'processos'
        



class Tipo(models.Model):
    nome = models.CharField(max_length=254)
    quantidade = models.IntegerField()
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
        db_table = "Tipo"
        
    
class Cliente(models.Model):
    cnpj =  BRCNPJField(blank=True, max_length=254, null=True, db_column='cnpj')
    nome = models.CharField(blank=True, null=True, max_length=500, db_column='nome')
    email = models.EmailField(blank=True, null=True, max_length=254, db_column='email')
    telefone = models.CharField(blank=True, null=True,  max_length=254, db_column='telefone')
    celular = models.CharField(blank=True, null=True,  max_length=254, db_column='celular')
    cod_cli = models.CharField(blank=True, null=True, max_length=50, default='', db_column='cod_cli')
    fax =  models.CharField(blank=True, null=True, max_length=50, db_column='fax')
    ie = models.CharField(blank=True, null=True, max_length=254, db_column='ie')
    cep = BRPostalCodeField(blank=True, null=True, db_column='cep')
    cidade = models.CharField(blank=True, null=True, max_length=120, db_column='cidade')
    estado = BRStateField(blank=True, null=True, default=None, max_length=50, db_column='estado')
    endereco = models.TextField(blank=True, null=True, db_column='endereco')
    obs = models.CharField(blank=True, null=True, max_length=254, default='', db_column='obs')
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
        db_table = "cliente"

class Fornecedor(models.Model):
    cnpj =  BRCNPJField(blank=True, max_length=254, null=True, db_column='cnpj')
    nome = models.CharField(blank=True, null=True, max_length=500, db_column='nome')
    email = models.EmailField(blank=True, null=True, max_length=254, db_column='email')
    telefone = models.CharField(blank=True, null=True,  max_length=254, db_column='telefone')
    celular = models.CharField(blank=True, null=True,  max_length=254, db_column='celular')
    cod_forn = models.CharField(blank=True, null=True, max_length=50, default='', db_column='cod_cli')
    fax =  models.CharField(blank=True, null=True, max_length=50, db_column='fax')
    ie = models.CharField(blank=True, null=True, max_length=254, db_column='ie')
    cep = BRPostalCodeField(blank=True, null=True, db_column='cep')
    cidade = models.CharField(blank=True, null=True, max_length=120, db_column='cidade')
    estado = BRStateField(blank=True, null=True, default=None, max_length=50, db_column='estado')
    endereco = models.TextField(blank=True, null=True, db_column='endereco')
    obs = models.CharField(blank=True, null=True, max_length=254, default='', db_column='obs')
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
        db_table = "Fornecedor"




class Material(models.Model):
    nome = models.CharField(blank=True, null=True, max_length=254, db_column='nome')
    custo = models.IntegerField(blank=True, null=True, db_column='custo')
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = _("Materiais")
        db_table = "material"

class Linha(models.Model):
    nome = models.CharField(max_length=254, db_column='nome')
    numero_inicial = models.IntegerField(primary_key=True,db_column="numero_inicial")
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
      db_table = 'linha'

class Formato(models.Model):
    nome = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.nome
class Rosca(models.Model):
    nome = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.nome

class Ferramenta(models.Model):
    nome = models.CharField(max_length=254, default='')
    material = models.ManyToManyField(Material, null=True, blank=True, db_column='cod_mat', related_name="material_ferramenta")
    arquivo_desenho = models.ImageField(_("Arquivo do desenho"), null=True, blank=True, upload_to='media/desenhos_pedidos', db_column="arquivo_desenho" )
    relatorio = models.ImageField(_("Relatorio do desenho"), null=True, blank=True, upload_to='media/relatorio_ferramenta', db_column="relatorio" )
    descricao = models.TextField(_("Descrição"), db_column="descricao", null=True, blank=True)
    passo = models.FloatField(_("Passo da Rosca(mm)"), null=True, blank=True, default=1, db_column="passo")
    rosca = models.ForeignKey(Rosca, on_delete=models.SET_NULL, db_column='tipo', related_name="ferramenta_rosca", null=True)
    diamnuceo = models.FloatField(_("Diâmetro do Núcleo"), null=True, blank=True, db_column="diametro_nucleo")
    diamtotal = models.FloatField(_("Diâmetro Total "), null=True, blank=True, db_column="diametro_total")
    qtd = models.IntegerField(_("Quantidade") ,null=True, blank=True, default=1, db_column="qtd")
    preco = models.FloatField(_("Valor por unidade"), null=True, blank=True, db_column="preco")
    diamrosca = models.CharField(_("Diâmetro da Rosca"),db_column="diametro_rosca", max_length=254, default='')
    tolerancia = models.CharField(_("Tolerância"),db_column="tolerancia", max_length=254, default='')
    norma = models.ForeignKey(Formato, on_delete=models.SET_NULL, db_column='formato', related_name="ferramenta_formato", null=True, default=0)
    processos = models.ManyToManyField(Processo, verbose_name=_("Processo(s)"), related_name="ferramenta_processo" )
    tempo = models.FloatField(_("Tempo"), null=True, blank=True, db_column="tempo")
    preco = models.FloatField(_("Preço por unidade"), null=True, blank=True, db_column="preco")
    
    
    
    history = HistoricalRecords()
    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'Ferramenta'



class Item(models.Model):
    TIPO = [
        ('canal reto', 'canal reto')
    ]
    nome = models.CharField(max_length=254, default='')
    descricao = models.TextField(_("Descrição"), db_column="descricao", null=True, blank=True)
    material = models.ManyToManyField(Material, null=True, blank=True, db_column='cod_mat', related_name="materialitem")
    qtd = models.IntegerField(_("Quantidade") ,null=True, blank=True, default=1, db_column="qtd")
    passo = models.FloatField(_("Passo da Rosca(mm)"), null=True, blank=True, default=1, db_column="passo")
    rosca = models.TextField(db_column="tipo", choices=TIPO, default='canal reto', null=True, blank=True)
    diamrosca = models.CharField(_("Diâmetro da Rosca"),db_column="diametro_rosca", max_length=254, default='')
    tolerancia = models.CharField(_("Tolerância"),db_column="tolerancia", max_length=254, default='')
    norma = models.ForeignKey(Formato, on_delete=models.SET_NULL, db_column='formato', related_name="format", null=True)
    processos = models.ManyToManyField(Processo, verbose_name=_("Processo(s)"), related_name="item_processo" )
    tempo = models.FloatField(_("Tempo"), null=True, blank=True, db_column="tempo")
    preco = models.FloatField(_("Preço"), null=True, blank=True, db_column="preco")
    arquivo_desenho = models.ImageField(_("Arquivo do desenho"), null=True, blank=True, upload_to='media/desenhos_pedidos', db_column="arquivo_desenho" )
    history = HistoricalRecords()
    
    def save(self, *args, **kwargs):
        fer = Ferramenta.objects.create(nome=self.nome, arquivo_desenho=self.arquivo_desenho)
        super().save(*args, **kwargs)
        for content in self.material.all():
            fer.material.add(content)
        
         

    def __str__(self):
        if self.preco and self.nome:
            return f"{self.nome} - Qtd: {self.qtd} - R${self.preco}"
        return self.nome
    class Meta:
        verbose_name_plural = _("Itens")
        db_table = 'itens'
   
class Cadastro_OS(models.Model):
    readonly_fields = ("Numero_Os","Data",)
    UNIDADE = [
        ('Peça', 'Peça'),
        ('Jogo', 'Jogo'),
        
    ]

    TIPO = [
        ('afiacao', 'afiação'),
        ('fabricacao', 'fabricação'),
        ('subfabricacao','subfabricação'),
        ('modificacao', 'modificação'),
        ('reconstrucao', 'reconstrução')
    ]
    
    Tipo = models.TextField(db_column="Tipo", choices=TIPO, default='afiacao',null=True, blank=True)
    Numero_Os = models.IntegerField( default=get_last_os , db_column="Numero_Os", editable=False)
    Cliente = models.ForeignKey(Cliente, swappable=False, on_delete=models.CASCADE, db_column='Id_Cliente', related_name="cliente_os", default=0)
    Data = models.DateField( null=True, blank=True, db_column="Data", default=now().strftime("%Y-%m-%d"), max_length=50)
    Prazo = models.DateField( null=True, blank=True, db_column="Prazo")
    gravacao = models.CharField(null=True, blank=True, max_length=50, db_column="gravacao")
    gravacao2 = models.CharField(null=True, blank=True, max_length=50, db_column="gravacao2")
    Ferramenta = models.TextField(null=True, blank=True,db_column="Ferramenta")
    Material = models.CharField(null=True, blank=True, max_length=50, db_column="Material")
    #Material = models.ForeignKey(Material ,null=True, blank=True, on_delete=models.CASCADE, db_column="Material",max_length=50)
    #Material = models.ManyToManyField(Material ,null=True, blank=True,db_column="Material",max_length=50)
    Especificacao = models.TextField(null=True, blank=True,db_column="Especificacao")
    Quantidade = models.IntegerField(null=True, blank=True,db_column="Quantidade")
    unidade = models.CharField(null=True, blank=True,max_length=50, db_column="unidade", choices=UNIDADE, default='peca')
    Desenho_Cliente = models.CharField(null=True, blank=True,db_column="Desenho_Cliente", max_length=50)
    Desenho_Pimentel = models.CharField(null=True, blank=True,db_column="Desenho_Pimentel",max_length=50)
    Numero_Nf = models.IntegerField(null=True, blank=True,db_column="Numero_Nf")
    Numero_Pedido = models.IntegerField(null=True, blank=True,db_column="Numero_Pedido")
    Data_Nf = models.DateField(null=True, blank=True,db_column="Data_Nf")
    Data_Pedido = models.DateField(null=True, blank=True,db_column="Data_Pedido")
    STATUS = models.CharField(null=True, blank=True, db_column="STATUS", max_length=70)
    Linha = models.ForeignKey(Linha, null=True, blank=True, db_column="id_Linha", on_delete=models.CASCADE, related_name="linha_os")
    data_digit = models.IntegerField(null=True, blank=True,db_column="data_digit", editable=False)
    history = HistoricalRecords()
    def __str__(self):
        return f"{self.Numero_Os} - {self.Cliente}"
    class Meta:
        db_table = 'cadastro_os'
        verbose_name = _("Ordem de Serviço")


class Pedido(models.Model):
    UNIDADE = [
        ('Peça', 'Peça'),
        ('Jogo', 'Jogo'),
        
    ]

    def get_last_pedido(self):
        largest = self.objects.values("numero_pedido").latest('numero_pedido')
        print(largest['numero_pedido'])
        if not largest:
            return 1
        return largest['numero_pedido'] + 1


    numero_pedido = models.IntegerField(default=get_last_pedido ,db_column="numero", editable=False)
    ano = models.IntegerField(_('ano'), default=datetime.now().year, db_column='ano', editable=False)
    Cliente = models.ForeignKey(Cliente, swappable=False, on_delete=models.CASCADE, db_column='id_cliente', related_name="cliente_pedido")
    item = models.ManyToManyField(Ferramenta, db_column='id_ferramenta', related_name="item_pedido")
    Especificacao = models.TextField(null=True, blank=True,db_column="especificacao")
    desenho = models.CharField(_("Obs. do desenho"), null=True, blank=True, max_length=150, db_column="desenho")
    unidade_pedido = models.CharField(null=True, blank=True,max_length=50, db_column="unidade", choices=UNIDADE, default='peca')
    qnt = models.IntegerField(_("Quantidade"), null=True, blank=True,db_column="qnt", editable=False)
    preco_pedido = models.FloatField(_("Preço"), null=True, blank=True, db_column="preco", editable=False)
    data_entrada = models.DateField(_("Data de Entrada"), null=True, blank=True, db_column="data_entrada", default=datetime.now().strftime("%Y-%m-%d"), max_length=50)
    qtd_acabada = models.IntegerField(_("Quantidade Acabada"), null=True, blank=True, db_column="qtd_acabada")
    os_pedido = models.ForeignKey(Cadastro_OS, null=True, blank=True,verbose_name=_("Ordem de Serviço"), on_delete=models.SET_NULL, db_column='id_os', related_name="pedido_os", editable=False)
    history = HistoricalRecords()
    class Meta:
        db_table = 'Pedido'
    def __str__(self):
        if self.preco_pedido and self.preco_pedido:
            return f"{self.Cliente} - R${self.preco_pedido} - Qtd: {self.qnt}"
        elif self.preco_pedido:
            return f"{self.Cliente} - R${self.preco_pedido}"
        elif self.qnt:
            return f"{self.Cliente} - Qtd: {self.qnt}"
        else:
            return f"{self.Cliente}" 
    def save(self, *args, **kwargs):
        if self.numero_pedido == None: self.numero_pedido = 0
        self.numero_pedido = self.numero_pedido + 1
        super().save(*args, **kwargs) 
        qnt = 0
        pricetotal = 0
        queryset = self.item.all().aggregate(
        total_price=models.Sum('preco'), total_qtd=models.Sum('qtd'))
        
        print("Preco pedido:")
        print(queryset["total_price"])
        self.preco_pedido = queryset["total_price"]
        self.qnt = queryset["total_qtd"]
        super().save(*args, **kwargs) 
        

class Orcamento(models.Model):
    numero = models.AutoField(primary_key=True, db_column='numero')
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL, db_column='id_cliente', related_name="cliente_orcamento")
    ano = models.IntegerField(_('ano'), default=datetime.now().year, db_column='ano')
    item = models.ManyToManyField(Ferramenta, verbose_name=_("Ferramenta(s)"), db_column='cod_ferramenta', related_name="item_orcamento")
    data = models.DateTimeField(default=now ,db_column='data')
    prazo_entrega = models.DateField(db_column='prazo_entrega', null=True, blank=True)
    prazo_pagamento = models.DateField(db_column='prazo_pagto', null=True, blank=True, )
    ipi = models.CharField(max_length=50, null=True, blank=True, db_column='ipi')
    icms = models.CharField(max_length=50, null=True, blank=True, db_column='icms')
    pedido_id = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL ,editable=False)
    qnt = models.IntegerField(_("Quantidade"), null=True, blank=True,db_column="qnt", editable=False)
    total = models.FloatField(_("Total"), null=True, blank=True, editable=False)
    history = HistoricalRecords()
    class Meta:
        db_table = 'orcamento' 
        verbose_name = _("Orçamento")
    def __str__(self):
        return f"{self.cliente}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        queryset = self.item.all().aggregate(
        total_price=models.Sum('preco'), total_qtd=models.Sum('qtd'))
        print(queryset["total_price"])
        self.qnt = queryset["total_qtd"]  
        self.total = queryset["total_price"]  
        super().save(*args, **kwargs)



class Historico_Os(models.Model):
    processo = models.ForeignKey(Processo, null=True, blank=True,verbose_name=_("Processo"), on_delete=models.SET_NULL, db_column='id_proc',  related_name="id_proc")
    os = models.ForeignKey(Cadastro_OS, null=True, blank=True,verbose_name=_("Ordem de Serviço"), on_delete=models.SET_NULL, related_name="id_os", db_column='id_os')
    inicio = models.TimeField(_("Início"), default=datetime.now().strftime('%H:%M:%S') ,auto_now=False, auto_now_add=False, db_column="inicio")
    fim =  models.TimeField(_("Fim"), null=True, blank=True,auto_now=False, auto_now_add=False, db_column="fim")
    ocorrencias = models.TextField(null=True, blank=True, db_column="ocorrencias")
    periodo = models.IntegerField(null=True, blank=True, db_column="periodo")
    data = models.DateTimeField(db_column='data', default=now, null=True, blank=True)
    qtd = models.IntegerField(null=True, blank=True,db_column="qtd")
    id_func = models.ForeignKey(User, null=True, blank=True, db_column="Colaborador", on_delete=models.SET_NULL)
    history = HistoricalRecords()
    def __str__(self):
        
        return f"O.S: {self.os.Numero_Os} - {self.processo} - {self.qtd}"
    
    class Meta:
        db_table = 'Historico_os'
        verbose_name = _("Localização O.S")
        verbose_name_plural = _("Localizar O.S")

    def save(self, *args, **kwargs):
        Cadastro_OS.objects.filter(pk=self.os.id).update(STATUS=self.processo.procname)
        super().save(*args, **kwargs)


class Product(models.Model):
    """
    Simple single type product.
    """

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name

    def get_price(self, request):
        return self.price

    @property
    def code(self):
        return str(self.id)


'''
class Diametro_interno(models.Model):
    maximo = models.FloatField(_("Máximo"), null=True, blank=True)
    minimo = models.FloatField(_("Minimo"), null=True, blank=True)
    media = models.FloatField(_("Média"),null=True, blank=True, default=((maximo+minimo)/2), editable=False)
    def __str__(self):
        return f"{self.maximo} ~ {self.minimo}"
    class Meta:
        db_table = 'diametro_interno'
        verbose_name = _("Diâmetro interno")
        verbose_name_plural = _("Diâmetros internos") 


class Diametro_externo(models.Model):
    maximo = models.FloatField(_("Máximo"), null=True, blank=True)
    minimo = models.FloatField(_("Minimo"), null=True, blank=True)
    media = models.FloatField(_("Média"), null=True, blank=True, default=((maximo+minimo)/2), editable=False)
    def __str__(self):
        return f" {self.maximo} ~ {self.minimo}"
    class Meta:
        db_table = 'diametro_externo'
        verbose_name = _("Diâmetro Externo")
        verbose_name_plural = _("Diâmetros Externos") 


class Calibrador(models.Model): 
    diametro_externo = models.ForeignKey(Diametro_interno, verbose_name=_("Diâmetro interno"),  null=True, blank=True, on_delete=models.CASCADE)
    diametro_interno = models.ForeignKey(Diametro_externo, verbose_name=_("Diâmetro externo"),  null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name=_("Cliente"), on_delete=models.CASCADE,  null=True, blank=True)

'''


 