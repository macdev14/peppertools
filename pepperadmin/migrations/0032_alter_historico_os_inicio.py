# Generated by Django 3.2.3 on 2021-06-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0031_auto_20210602_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='10:35:05', verbose_name='Início'),
        ),
    ]