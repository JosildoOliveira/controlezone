# Generated by Django 4.1 on 2022-10-25 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proc', '0018_alter_processos_processo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processos',
            name='processo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proc.empresa'),
        ),
    ]