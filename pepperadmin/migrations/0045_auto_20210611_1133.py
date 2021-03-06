# Generated by Django 3.2.3 on 2021-06-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0044_auto_20210611_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='arquivo_desenho',
        ),
        migrations.AddField(
            model_name='item',
            name='arquivo_desenho',
            field=models.ImageField(blank=True, db_column='arquivo_desenho', null=True, upload_to='media/desenhos_pedidos', verbose_name='Arquivo do desenho'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='11:32:59', verbose_name='Início'),
        ),
    ]
