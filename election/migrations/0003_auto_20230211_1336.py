# Generated by Django 3.2.13 on 2023-02-11 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_remove_contestant_ballotbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion_name', models.CharField(max_length=90)),
            ],
        ),
        migrations.AddField(
            model_name='contestant',
            name='postion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='election.postions'),
        ),
    ]
