# Generated by Django 3.1.4 on 2022-04-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customersapp', '0006_auto_20220421_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customersapp.userprofile'),
        ),
    ]
