# Generated by Django 2.1.2 on 2018-11-29 02:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20181129_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='laddrmatch',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 2, 33, 49, 897146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usermatch',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 2, 33, 49, 897146, tzinfo=utc)),
        ),
    ]