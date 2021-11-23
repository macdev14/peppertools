# Generated by Django 3.1.3 on 2021-11-15 15:18

from django.db import migrations, models
import django.db.models.deletion
import oscar.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0070_auto_20211101_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ferramenta',
            old_name='diamnuceo',
            new_name='diametro_nucleo',
        ),
        migrations.RenameField(
            model_name='historicalferramenta',
            old_name='diamnuceo',
            new_name='diametro_nucleo',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='diamrosca',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='diamtotal',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='material',
        ),
        migrations.RemoveField(
            model_name='ferramenta',
            name='norma',
        ),
        migrations.RemoveField(
            model_name='historicalferramenta',
            name='diamrosca',
        ),
        migrations.RemoveField(
            model_name='historicalferramenta',
            name='diamtotal',
        ),
        migrations.RemoveField(
            model_name='historicalferramenta',
            name='norma',
        ),
        migrations.RemoveField(
            model_name='historicalitem',
            name='diamrosca',
        ),
        migrations.RemoveField(
            model_name='historicalitem',
            name='norma',
        ),
        migrations.RemoveField(
            model_name='item',
            name='diamrosca',
        ),
        migrations.RemoveField(
            model_name='item',
            name='material',
        ),
        migrations.RemoveField(
            model_name='item',
            name='norma',
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='diametro_externo',
            field=models.FloatField(blank=True, db_column='diametro_externo', null=True, verbose_name='Diâmetro Externo '),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='truncamento_crista_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_maximo', null=True, verbose_name='Truncamento da Crista (máximo)'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='truncamento_crista_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_minimo', null=True, verbose_name='Truncamento da Crista (mínimo)'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='truncamento_raiz_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_maximo', null=True, verbose_name='Truncamento da Raíz (máximo)'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='truncamento_raiz_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_minimo', null=True, verbose_name='Truncamento da Raíz (mínimo)'),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='diametro_externo',
            field=models.FloatField(blank=True, db_column='diametro_externo', null=True, verbose_name='Diâmetro Externo '),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='truncamento_crista_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_maximo', null=True, verbose_name='Truncamento da Crista (máximo)'),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='truncamento_crista_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_minimo', null=True, verbose_name='Truncamento da Crista (mínimo)'),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='truncamento_raiz_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_maximo', null=True, verbose_name='Truncamento da Raíz (máximo)'),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='truncamento_raiz_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_minimo', null=True, verbose_name='Truncamento da Raíz (mínimo)'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='diametro_externo',
            field=models.FloatField(blank=True, db_column='diametro_externo', null=True, verbose_name='Diâmetro Externo '),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='diametro_nucleo',
            field=models.FloatField(blank=True, db_column='diametro_nucleo', null=True, verbose_name='Diâmetro do Núcleo'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='truncamento_crista_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_maximo', null=True, verbose_name='Truncamento da Crista (máximo)'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='truncamento_crista_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_minimo', null=True, verbose_name='Truncamento da Crista (mínimo)'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='truncamento_raiz_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_maximo', null=True, verbose_name='Truncamento da Raíz (máximo)'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='truncamento_raiz_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_minimo', null=True, verbose_name='Truncamento da Raíz (mínimo)'),
        ),
        migrations.AddField(
            model_name='item',
            name='diametro_externo',
            field=models.FloatField(blank=True, db_column='diametro_externo', null=True, verbose_name='Diâmetro Externo '),
        ),
        migrations.AddField(
            model_name='item',
            name='diametro_nucleo',
            field=models.FloatField(blank=True, db_column='diametro_nucleo', null=True, verbose_name='Diâmetro do Núcleo'),
        ),
        migrations.AddField(
            model_name='item',
            name='truncamento_crista_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_maximo', null=True, verbose_name='Truncamento da Crista (máximo)'),
        ),
        migrations.AddField(
            model_name='item',
            name='truncamento_crista_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_crista_minimo', null=True, verbose_name='Truncamento da Crista (mínimo)'),
        ),
        migrations.AddField(
            model_name='item',
            name='truncamento_raiz_maximo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_maximo', null=True, verbose_name='Truncamento da Raíz (máximo)'),
        ),
        migrations.AddField(
            model_name='item',
            name='truncamento_raiz_minimo',
            field=models.FloatField(blank=True, db_column='truncamento_raiz_minimo', null=True, verbose_name='Truncamento da Raíz (mínimo)'),
        ),
        migrations.AlterField(
            model_name='cadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-11-15', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='qtd',
            field=models.IntegerField(blank=True, db_column='quantidade', default=1, null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='historicalcadastro_os',
            name='Data',
            field=models.DateField(blank=True, db_column='Data', default='2021-11-15', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalferramenta',
            name='qtd',
            field=models.IntegerField(blank=True, db_column='quantidade', default=1, null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='12:18:20', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='rosca',
            field=models.ForeignKey(blank=True, db_column='tipo', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.rosca'),
        ),
        migrations.AlterField(
            model_name='historicalpedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-11-15', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='12:18:20', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='item',
            name='arquivo_desenho',
            field=models.FileField(blank=True, db_column='arquivo_desenho', null=True, upload_to=oscar.utils.models.get_image_upload_path, verbose_name='Arquivo do desenho'),
        ),
        migrations.AlterField(
            model_name='item',
            name='rosca',
            field=models.ForeignKey(db_column='tipo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_rosca', to='pepperadmin.rosca'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.DateField(blank=True, db_column='data_entrada', default='2021-11-15', max_length=50, null=True, verbose_name='Data de Entrada'),
        ),
    ]
