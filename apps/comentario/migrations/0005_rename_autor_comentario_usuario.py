# Generated by Django 4.0.6 on 2022-08-30 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0004_alter_comentario_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='autor',
            new_name='usuario',
        ),
    ]