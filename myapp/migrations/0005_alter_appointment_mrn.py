# Generated by Django 5.1.6 on 2025-02-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_appointment_date_alter_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='mrn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
