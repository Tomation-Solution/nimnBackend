# Generated by Django 3.2.13 on 2023-02-07 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_membershipgrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberEmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion_title', models.CharField(max_length=200)),
                ('employment_from', models.DateField(blank=True, default=None, null=True)),
                ('employment_to', models.DateField(blank=True, default=None, null=True)),
                ('employer_name_and_addresse', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='memeber',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='memeber',
            name='citizenship',
            field=models.CharField(default='', max_length=24),
        ),
        migrations.AddField(
            model_name='memeber',
            name='dob',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='memeber',
            name='telephone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.CreateModel(
            name='MemberEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_institution', models.TextField(default='')),
                ('major', models.TextField(default='')),
                ('degree', models.CharField(default='', max_length=50)),
                ('language', models.CharField(default='', max_length=50)),
                ('reading', models.CharField(default='', max_length=50)),
                ('speaking', models.CharField(default='', max_length=50)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
            ],
        ),
    ]
