# Generated by Django 3.2.3 on 2021-06-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0058_auto_20210616_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_os',
            name='data_digit',
            field=models.IntegerField(blank=True, db_column='data_digit', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalcadastro_os',
            name='data_digit',
            field=models.IntegerField(blank=True, db_column='data_digit', editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-06-18', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-06-18', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='17:01:17', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historicalpedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-06-18', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='17:01:17', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-06-18', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
    ]
