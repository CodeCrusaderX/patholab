# Generated by Django 5.1.1 on 2024-11-23 06:47

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathoapp', '0028_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiv',
            fields=[
                ('test_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('test_date', models.DateField(default=datetime.datetime.now)),
                ('hiv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('other_test', models.CharField(blank=True, max_length=100, null=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('normal_value', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('patientname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pathoapp.patientmaster')),
            ],
        ),
    ]
