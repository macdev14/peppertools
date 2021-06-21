# Generated by Django 3.2.3 on 2021-06-14 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0053_auto_20210614_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-06-14', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro_os',
            name='Linha',
            field=models.ForeignKey(blank=True, db_column='id_Linha', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='linha_os', to='pepperadmin.linha'),
        ),
        migrations.AlterField(
            model_name='cadastro_os',
            name='Prazo',
            field=models.DateField(blank=True, db_column='Prazo', null=True),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='16:38:38', verbose_name='Início'),
        ),
    ]