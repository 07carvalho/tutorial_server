# Generated by Django 2.2.6 on 2019-10-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='latency',
            field=models.FloatField(),
        ),
    ]