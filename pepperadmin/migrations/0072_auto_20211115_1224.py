# Generated by Django 3.1.3 on 2021-11-15 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pepperadmin', '0071_auto_20211115_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferramenta',
            name='material',
            field=models.ManyToManyField(blank=True, db_column='cod_mat', related_name='material_ferramenta', to='pepperadmin.Material'),
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='norma',
            field=models.ForeignKey(db_column='formato', default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ferramenta_formato', to='pepperadmin.formato'),
        ),
        migrations.AddField(
            model_name='historicalferramenta',
            name='norma',
            field=models.ForeignKey(blank=True, db_column='formato', db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.formato'),
        ),
        migrations.AddField(
            model_name='historicalitem',
            name='norma',
            field=models.ForeignKey(blank=True, db_column='formato', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pepperadmin.formato'),
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.ManyToManyField(blank=True, db_column='cod_mat', related_name='materialitem', to='pepperadmin.Material'),
        ),
        migrations.AddField(
            model_name='item',
            name='norma',
            field=models.ForeignKey(db_column='formato', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='format_item', to='pepperadmin.formato'),
        ),
        migrations.AlterField(
            model_name='historicalhistorico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='12:24:47', verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='historico_os',
            name='inicio',
            field=models.TimeField(db_column='inicio', default='12:24:47', verbose_name='Início'),
        ),
    ]
