# Generated by Django 4.0.6 on 2022-08-29 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0003_alter_noticia_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default='images/default.png', upload_to='images'),
        ),
    ]
