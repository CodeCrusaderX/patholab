# Generated by Django 5.1.1 on 2024-10-07 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathoapp', '0011_bloodsugartest_delete_bloodtest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BloodSugarTest',
        ),
    ]
