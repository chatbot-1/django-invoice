# Generated by Django 4.1.7 on 2023-08-20 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myInvoice', '0002_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AlterField(
            model_name='add_service',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myInvoice.client'),
        ),
    ]
