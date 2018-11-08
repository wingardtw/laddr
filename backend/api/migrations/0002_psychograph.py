# Generated by Django 2.0.3 on 2018-08-23 00:00

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psychograph',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('johnny_rank', models.IntegerField(default=0)),
                ('spike_rank', models.IntegerField(default=0)),
                ('timmy_rank', models.IntegerField(default=0)),
            ],
        ),
    ]
