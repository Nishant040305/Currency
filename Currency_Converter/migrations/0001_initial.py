# Generated by Django 4.2.5 on 2023-11-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='favPain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromCode', models.CharField(max_length=5)),
                ('toCode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcurrencyCode', models.CharField(max_length=5)),
                ('fAmount', models.CharField(max_length=50)),
                ('tcurrencyCode', models.CharField(max_length=5)),
                ('tAmount', models.CharField(max_length=50)),
            ],
        ),
    ]