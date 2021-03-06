# Generated by Django 3.2.3 on 2021-06-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0039_auto_20210602_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:41:36', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-06-02', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
    ]
