# Generated by Django 4.1 on 2022-08-19 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='anonse',
        ),
    ]
