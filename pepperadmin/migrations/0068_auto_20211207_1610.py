# Generated by Django 3.1.3 on 2021-12-07 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pepperadmin', '0067_auto_20210830_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalhistorico_os',
            name='colaborador',
            field=models.ForeignKey(blank=True, db_column='colaborador', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
        migrations.AddField(
            model_name='historico_os',
            name='colaborador',
            field=models.ForeignKey(blank=True, db_column='colaborador', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_func', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-12-07', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='material',
            field=models.ManyToManyField(blank=True, db_column='cod_mat', related_name='material_ferramenta', to='pepperadmin.Material'),
        ),
        migrations.AlterField(
            model_name='historicalcadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-12-07', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:10:35', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historicalpedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-12-07', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:10:35', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.ManyToManyField(blank=True, db_column='cod_mat', related_name='materialitem', to='pepperadmin.Material'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-12-07', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
    ]
