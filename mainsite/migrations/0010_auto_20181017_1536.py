# Generated by Django 2.1.2 on 2018-10-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0009_auto_20181017_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
