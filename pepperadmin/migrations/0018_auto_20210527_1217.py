# Generated by Django 3.2.3 on 2021-05-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0017_auto_20210526_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, db_column='celular', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, db_column='telefone', max_length=254, null=True),
        ),
    ]
