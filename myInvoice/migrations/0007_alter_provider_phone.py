# Generated by Django 4.1.7 on 2023-08-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myInvoice', '0006_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
