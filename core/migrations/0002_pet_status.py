# Generated by Django 3.0.7 on 2021-10-20 01:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('1', 'Disponível'), ('2', 'Reservado'), ('3', 'Adotado')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
