# Generated by Django 3.0.5 on 2020-06-18 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200618_0202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['-releaseDate']},
        ),
    ]
