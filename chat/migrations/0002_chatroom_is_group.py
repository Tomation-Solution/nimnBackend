# Generated by Django 3.2.13 on 2023-03-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
    ]
