# Generated by Django 3.2.3 on 2021-05-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0023_alter_cliente_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(blank=True, db_column='cidade', max_length=120, null=True),
        ),
    ]
