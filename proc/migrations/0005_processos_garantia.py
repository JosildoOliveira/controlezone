# Generated by Django 4.1 on 2022-09-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proc', '0004_alter_empresa_cnpj_alter_empresa_empresa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='processos',
            name='garantia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Garantia'),
        ),
    ]
