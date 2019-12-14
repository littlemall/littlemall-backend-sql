# Generated by Django 2.1.3 on 2019-11-28 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0003_auto_20191122_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodssku',
            name='goods_id',
        ),
        migrations.AddField(
            model_name='goodssku',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='as_good', to='good.Goods'),
        ),
    ]
