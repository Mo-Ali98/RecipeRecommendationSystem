# Generated by Django 2.2.6 on 2020-03-23 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_healthdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='healthdata',
            options={'ordering': ('-date',)},
        ),
    ]
