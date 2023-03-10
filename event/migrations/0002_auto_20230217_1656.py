# Generated by Django 3.2.13 on 2023-02-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_extra_details',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='event',
            name='organiser_extra_info',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='organiser_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
