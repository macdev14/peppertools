# Generated by Django 3.2.3 on 2021-06-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0046_auto_20210611_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='12:11:33', verbose_name='Início'),
        ),
    ]
