# Generated by Django 3.2.13 on 2023-02-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_memberemploymenthistory_member'),
        ('election', '0005_remove_ballotbox_members_that_has_cast_thier_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='postions',
            name='members_that_has_cast_thier_vote',
            field=models.ManyToManyField(to='account.Memeber'),
        ),
    ]
