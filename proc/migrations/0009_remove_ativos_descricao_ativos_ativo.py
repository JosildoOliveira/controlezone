# Generated by Django 4.1 on 2022-10-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proc', '0008_alter_ativos_vlr_custo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ativos',
            name='descricao',
        ),
        migrations.AddField(
            model_name='ativos',
            name='ativo',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ativo'),
        ),
    ]
