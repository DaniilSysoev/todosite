# Generated by Django 4.1.7 on 2023-03-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]
