# Generated by Django 5.1.1 on 2025-02-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathoapp', '0036_alter_urine_test_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiv',
            name='test_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
