# Generated by Django 3.2.13 on 2023-02-08 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_memberemploymenthistory_member'),
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundAProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('about', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SupportProjectInKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('about', models.TextField(default='')),
                ('member', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
        migrations.CreateModel(
            name='SupportProjectInCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paystack_key', models.TextField(default='')),
                ('is_paid', models.BooleanField(default=False)),
                ('member', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
    ]
