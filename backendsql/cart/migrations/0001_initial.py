# Generated by Django 2.1.3 on 2020-01-16 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feuser', '0004_auto_20200115_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feuser.FeAddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feuser.Feuser')),
            ],
        ),
    ]
