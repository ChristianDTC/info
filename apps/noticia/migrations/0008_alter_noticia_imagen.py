# Generated by Django 4.0.6 on 2022-08-30 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0007_rename_autor_noticia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='noticia/default.png', upload_to='noticia'),
        ),
    ]