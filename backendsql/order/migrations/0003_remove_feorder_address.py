# Generated by Django 2.1.3 on 2020-01-17 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_feorder_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feorder',
            name='address',
        ),
    ]
