# Generated by Django 3.0.5 on 2020-06-18 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200618_0205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={},
        ),
        migrations.RemoveField(
            model_name='variant',
            name='releaseDate',
        ),
    ]
