# Generated by Django 3.2.13 on 2023-02-08 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_fundaproject_supportprojectincash_supportprojectinkind'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportprojectincash',
            name='project',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extras.fundaproject'),
        ),
        migrations.AddField(
            model_name='supportprojectinkind',
            name='project',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extras.fundaproject'),
        ),
    ]
