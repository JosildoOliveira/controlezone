# Generated by Django 4.1 on 2022-10-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proc', '0011_alter_ativos_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ativos',
            name='centro_custo',
            field=models.CharField(blank=True, choices=[('Secretaria', 'Secretaria'), ('Administrativo', 'Administrativo'), ('Técnico', 'Técnico')], default='Administrativo', max_length=100, null=True),
        ),
    ]