# Generated by Django 2.1.3 on 2020-01-17 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feorder',
            name='cart',
        ),
    ]