# Generated by Django 3.2.13 on 2023-02-09 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_memberemploymenthistory_member'),
        ('extras', '0006_reissuanceofcertificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reissuanceofcertificate',
            name='member',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.memeber'),
        ),
    ]
