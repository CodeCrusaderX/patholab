# Generated by Django 5.1.1 on 2025-02-22 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathoapp', '0048_tempdoctortest_delete_tempalltest'),
    ]

    operations = [
        migrations.AddField(
            model_name='haematology',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pathoapp.doctor'),
        ),
    ]
