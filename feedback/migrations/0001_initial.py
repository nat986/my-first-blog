# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-20 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_name', models.CharField(max_length=200)),
                ('current_session', models.CharField(choices=[('S1', 'Session 1'), ('S2', 'Session 2'), ('S3', 'Session 3'), ('S4', 'Session 4'), ('RP', 'Ramp')], default='S1', max_length=2)),
                ('text', models.TextField()),
                ('notes', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
