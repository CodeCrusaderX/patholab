# Generated by Django 5.1.1 on 2025-02-22 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathoapp', '0046_delete_tempalltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempAllTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=50)),
                ('patient_id', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile_no', models.CharField(max_length=15)),
                ('test_date', models.DateField()),
                ('test_name', models.CharField(max_length=100)),
            ],
        ),
    ]
