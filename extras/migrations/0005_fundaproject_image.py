# Generated by Django 3.2.13 on 2023-02-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0004_fundaproject_amount_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundaproject',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
