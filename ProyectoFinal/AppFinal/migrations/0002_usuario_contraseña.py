# Generated by Django 5.0.7 on 2024-08-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
