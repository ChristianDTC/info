# Generated by Django 4.0.6 on 2022-08-30 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0006_alter_noticia_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='autor',
            new_name='usuario',
        ),
    ]