# Generated by Django 3.1.3 on 2021-12-10 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pepperadmin', '0068_auto_20211207_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-12-10', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-12-10', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:46:57', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='periodo',
            field=models.IntegerField(blank=True, db_column='periodo', default=1, null=True),
        ),
        migrations.AlterField(
            model_name='historicalpedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-12-10', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='colaborador',
            field=models.ForeignKey(db_column='colaborador', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_func', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:46:57', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='os',
            field=models.ForeignKey(db_column='id_os', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_os', to='pepperadmin.cadastro_os', verbose_name='Ordem de Serviço'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='periodo',
            field=models.IntegerField(blank=True, db_column='periodo', default=1, null=True),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='processo',
            field=models.ForeignKey(db_column='id_proc', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_proc', to='pepperadmin.processo', verbose_name='Processo'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-12-10', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
    ]