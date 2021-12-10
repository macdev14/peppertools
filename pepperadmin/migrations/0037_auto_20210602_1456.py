# Generated by Django 3.2.3 on 2021-06-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0036_auto_20210602_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='arquivo_desenho',
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='14:56:09', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='ano',
            field=models.IntegerField(db_column='ano', default=2021, editable=False, verbose_name='ano'),
        ),
    ]
