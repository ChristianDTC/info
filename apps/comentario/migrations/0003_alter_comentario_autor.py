# Generated by Django 4.0.6 on 2022-08-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.CharField(max_length=20),
        ),
    ]
