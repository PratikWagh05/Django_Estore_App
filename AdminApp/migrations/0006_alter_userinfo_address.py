# Generated by Django 4.1.2 on 2022-12-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_userinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=40),
        ),
    ]