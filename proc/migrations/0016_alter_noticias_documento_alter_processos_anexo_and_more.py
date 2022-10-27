# Generated by Django 4.1 on 2022-10-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proc', '0015_noticias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='documento',
            field=models.FileField(blank=True, help_text='Breve descrição do documento', null=True, upload_to='media', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='processos',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Arquivo do Processo'),
        ),
        migrations.AlterField(
            model_name='processos',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='processos',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
    ]