# Generated by Django 3.1.4 on 2022-04-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customersapp', '0002_auto_20220414_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=True),
        ),
    ]
