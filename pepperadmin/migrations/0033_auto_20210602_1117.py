# Generated by Django 3.2.3 on 2021-06-02 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0032_alter_historico_os_inicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='numero_pedido',
            new_name='numero',
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='11:17:46', verbose_name='Início'),
        ),
    ]