# Generated by Django 4.0.6 on 2022-08-13 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentario', '0001_initial'),
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticia.noticia'),
        ),
    ]
