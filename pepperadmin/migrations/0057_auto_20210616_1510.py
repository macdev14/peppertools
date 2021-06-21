# Generated by Django 3.2.3 on 2021-06-16 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pepperadmin.models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pepperadmin', '0056_auto_20210614_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-06-16', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='15:10:32', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-06-16', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.CreateModel(
            name='HistoricalProcesso',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('procname', models.CharField(blank=True, db_column='Nome', max_length=254, null=True, verbose_name='Nome')),
                ('Tempo_Objetivo', models.TimeField(blank=True, db_column='Tempo_Objetivo', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical processo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPedido',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('numero_pedido', models.IntegerField(db_column='numero', editable=False)),
                ('ano', models.IntegerField(db_column='ano', default=2021, editable=False, verbose_name='ano')),
                ('Especificacao', models.TextField(blank=True, db_column='especificacao', null=True)),
                ('desenho', models.CharField(blank=True, db_column='desenho', max_length=150, null=True, verbose_name='Obs. do desenho')),
                ('unidade_pedido', models.CharField(blank=True, choices=[('Peça', 'Peça'), ('Jogo', 'Jogo')], db_column='unidade', default='peca', max_length=50, null=True)),
                ('qnt', models.IntegerField(blank=True, db_column='qnt', editable=False, null=True, verbose_name='Quantidade')),
                ('preco_pedido', models.FloatField(blank=True, db_column='preco', editable=False, null=True, verbose_name='Preço')),
                ('data_entrada', models.DateField(blank=True, db_column='data_entrada', default='2021-06-16', max_length=50, null=True, verbose_name='Data de Entrada')),
                ('qtd_acabada', models.IntegerField(blank=True, db_column='qtd_acabada', null=True, verbose_name='Quantidade Acabada')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Cliente', models.ForeignKey(blank=True, db_column='id_cliente', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('os_pedido', models.ForeignKey(blank=True, db_column='id_os', db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.cadastro_os', verbose_name='Ordem de Serviço')),
            ],
            options={
                'verbose_name': 'historical pedido',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrcamento',
            fields=[
                ('numero', models.IntegerField(blank=True, db_column='numero', db_index=True)),
                ('ano', models.IntegerField(db_column='ano', default=2021, verbose_name='ano')),
                ('data', models.DateTimeField(db_column='data', default=django.utils.timezone.now)),
                ('prazo_entrega', models.DateField(blank=True, db_column='prazo_entrega', null=True)),
                ('prazo_pagamento', models.DateField(blank=True, db_column='prazo_pagto', null=True)),
                ('ipi', models.CharField(blank=True, db_column='ipi', max_length=50, null=True)),
                ('icms', models.CharField(blank=True, db_column='icms', max_length=50, null=True)),
                ('qnt', models.IntegerField(blank=True, db_column='qnt', editable=False, null=True, verbose_name='Quantidade')),
                ('total', models.FloatField(blank=True, editable=False, null=True, verbose_name='Total')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cliente', models.ForeignKey(blank=True, db_column='id_cliente', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pedido_id', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.pedido')),
            ],
            options={
                'verbose_name': 'historical Orçamento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalItem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=254)),
                ('descricao', models.TextField(blank=True, db_column='descricao', null=True, verbose_name='Descrição')),
                ('qtd', models.IntegerField(blank=True, db_column='qtd', default=1, null=True, verbose_name='Quantidade')),
                ('preco', models.FloatField(blank=True, db_column='preco', null=True, verbose_name='Preço')),
                ('arquivo_desenho', models.TextField(blank=True, db_column='arquivo_desenho', max_length=100, null=True, verbose_name='Arquivo do desenho')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical item',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalHistorico_Os',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('inicio', models.TimeField(db_column='inicio', default='15:10:32', verbose_name='Início')),
                ('fim', models.TimeField(blank=True, db_column='fim', null=True, verbose_name='Fim')),
                ('ocorrencias', models.TextField(blank=True, db_column='ocorrencias', null=True)),
                ('periodo', models.IntegerField(blank=True, db_column='periodo', null=True)),
                ('data', models.DateTimeField(blank=True, db_column='data', default=django.utils.timezone.now, null=True)),
                ('qtd', models.IntegerField(blank=True, db_column='qtd', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('os', models.ForeignKey(blank=True, db_column='id_os', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.cadastro_os', verbose_name='Ordem de Serviço')),
                ('processo', models.ForeignKey(blank=True, db_column='id_proc', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.processo', verbose_name='Processo')),
            ],
            options={
                'verbose_name': 'historical Localização O.S',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCadastro_OS',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Tipo', models.TextField(blank=True, choices=[('afiacao', 'afiação'), ('fabricacao', 'fabricação'), ('subfabricacao', 'subfabricação'), ('modificacao', 'modificação'), ('reconstrucao', 'reconstrução')], db_column='Tipo', default='afiacao', null=True)),
                ('Numero_Os', models.IntegerField(db_column='Numero_Os', default=pepperadmin.models.get_last_os, editable=False)),
                ('Data', models.DateField(blank=True, db_column='Data', default='2021-06-16', max_length=50, null=True)),
                ('Prazo', models.DateField(blank=True, db_column='Prazo', null=True)),
                ('gravacao', models.CharField(blank=True, db_column='gravacao', max_length=50, null=True)),
                ('gravacao2', models.CharField(blank=True, db_column='gravacao2', max_length=50, null=True)),
                ('Ferramenta', models.TextField(blank=True, db_column='Ferramenta', null=True)),
                ('Material', models.CharField(blank=True, db_column='Material', max_length=50, null=True)),
                ('Especificacao', models.TextField(blank=True, db_column='Especificacao', null=True)),
                ('Quantidade', models.IntegerField(blank=True, db_column='Quantidade', null=True)),
                ('unidade', models.CharField(blank=True, choices=[('Peça', 'Peça'), ('Jogo', 'Jogo')], db_column='unidade', default='peca', max_length=50, null=True)),
                ('Desenho_Cliente', models.CharField(blank=True, db_column='Desenho_Cliente', max_length=50, null=True)),
                ('Desenho_Pimentel', models.CharField(blank=True, db_column='Desenho_Pimentel', max_length=50, null=True)),
                ('Numero_Nf', models.IntegerField(blank=True, db_column='Numero_Nf', null=True)),
                ('Numero_Pedido', models.IntegerField(blank=True, db_column='Numero_Pedido', null=True)),
                ('Data_Nf', models.DateField(blank=True, db_column='Data_Nf', null=True)),
                ('Data_Pedido', models.DateField(blank=True, db_column='Data_Pedido', null=True)),
                ('STATUS', models.CharField(blank=True, db_column='STATUS', max_length=70, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Cliente', models.ForeignKey(blank=True, db_column='Id_Cliente', db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.cliente')),
                ('Linha', models.ForeignKey(blank=True, db_column='id_Linha', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.linha')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Ordem de Serviço',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]