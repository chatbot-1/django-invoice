# Generated by Django 4.1.7 on 2023-08-13 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=50)),
                ('gst', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myInvoice.client')),
            ],
        ),
        migrations.CreateModel(
            name='Add_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp2_name', models.CharField(max_length=50)),
                ('handle_by', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('account', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myInvoice.client')),
            ],
        ),
    ]
