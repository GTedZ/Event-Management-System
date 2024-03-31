# Generated by Django 5.0.2 on 2024-03-31 07:53

import django.contrib.auth.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0006_alter_userprofile_options_alter_userprofile_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('event_tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_tag_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('event_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=100)),
                ('event_description', models.CharField(max_length=100)),
                ('event_link', models.URLField()),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('event_likes_count', models.IntegerField()),
                ('event_created_on', models.DateTimeField()),
                ('event_modified_on', models.DateTimeField()),
                ('event_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_created', to='ems.userprofile')),
                ('event_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_modified', to='ems.userprofile')),
                ('event_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.eventtag')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.eventtype')),
                ('event_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.location')),
            ],
        ),
        migrations.CreateModel(
            name='LikedEvents',
            fields=[
                ('liked_events_id', models.AutoField(primary_key=True, serialize=False)),
                ('liked_events_liked_on', models.DateTimeField()),
                ('liked_events_event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems.event')),
                ('liked_events_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_events', to='ems.userprofile')),
            ],
        ),
    ]
