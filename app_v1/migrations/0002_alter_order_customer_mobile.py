# Generated by Django 3.2 on 2021-04-30 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_mobile',
            field=models.IntegerField(),
        ),
    ]