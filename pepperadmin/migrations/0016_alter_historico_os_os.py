# Generated by Django 3.2.3 on 2021-05-25 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0015_alter_historico_os_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico_os',
            name='os',
            field=models.ForeignKey(blank=True, db_column='id_os', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_os', to='pepperadmin.cadastro_os', verbose_name='Ordem de Serviço'),
        ),
    ]
