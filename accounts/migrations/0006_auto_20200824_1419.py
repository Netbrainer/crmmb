# Generated by Django 3.1 on 2020-08-24 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200824_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
    ]
