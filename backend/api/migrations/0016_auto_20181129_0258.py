# Generated by Django 2.1.2 on 2018-11-29 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20181129_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laddrmatch',
            name='expires_at',
        ),
        migrations.RemoveField(
            model_name='usermatch',
            name='expires_at',
        ),
    ]