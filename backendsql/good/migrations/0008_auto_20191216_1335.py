# Generated by Django 2.1.3 on 2019-12-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0007_auto_20191214_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
