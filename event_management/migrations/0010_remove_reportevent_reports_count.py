# Generated by Django 5.0.2 on 2024-04-06 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0009_reportevent_reports_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportevent',
            name='reports_count',
        ),
    ]
