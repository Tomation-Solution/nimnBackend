# Generated by Django 3.2.13 on 2023-02-06 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_membershipgrade'),
        ('Dueapp', '0002_due_dues_for_membership_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='due',
            name='chapters',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.chapters'),
        ),
        migrations.AlterField(
            model_name='due',
            name='dues_for_membership_grade',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.membershipgrade'),
        ),
    ]
