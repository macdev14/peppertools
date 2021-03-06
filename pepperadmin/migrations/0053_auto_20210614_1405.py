# Generated by Django 3.2.3 on 2021-06-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0052_auto_20210614_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ferramenta',
            name='mm',
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='arquivo_desenho',
            field=models.ImageField(blank=True, db_column='arquivo_desenho', null=True, upload_to='media/desenhos_pedidos', verbose_name='Arquivo do desenho'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='material',
            field=models.ManyToManyField(blank=True, db_column='cod_mat', null=True, related_name='material_ferramenta', to='pepperadmin.Material'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='relatorio',
            field=models.ImageField(blank=True, db_column='relatorio', null=True, upload_to='media/relatorio_ferramenta', verbose_name='Relatorio do desenho'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='nome',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='14:05:10', verbose_name='Início'),
        ),
    ]
