# Generated by Django 5.1.6 on 2025-02-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_appointment_appt_scheduled_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
