# Generated by Django 3.0.7 on 2020-09-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaurabhComputerApp', '0007_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
