# Generated by Django 2.1.2 on 2018-10-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20181017_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]
