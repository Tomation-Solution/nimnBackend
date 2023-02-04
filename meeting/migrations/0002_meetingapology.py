# Generated by Django 3.2.13 on 2023-02-03 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingApology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='I sorry i can attend')),
                ('meeting', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='meeting.meeting')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
    ]
