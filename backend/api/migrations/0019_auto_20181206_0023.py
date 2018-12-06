# Generated by Django 2.1.2 on 2018-12-06 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20181206_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchingpreference',
            name='rank',
            field=models.IntegerField(blank=True, choices=[(0, 'Bronze V'), (1, 'Bronze IV'), (2, 'Bronze III'), (3, 'Bronze II'), (4, 'Bronze I'), (5, 'Silver V'), (6, 'Silver IV'), (7, 'Silver III'), (8, 'Silver II'), (9, 'Silver I'), (10, 'Gold V'), (11, 'Gold IV'), (12, 'Gold III'), (13, 'Gold II'), (14, 'Gold I'), (15, 'Platinum V'), (16, 'Platinum IV '), (17, 'Platinum III'), (18, 'Platinum II'), (19, 'Platinum I'), (20, 'Diamond V'), (21, 'Diamond IV'), (22, 'Diamond III'), (23, 'Diamond II'), (24, 'Diamond I'), (25, 'Challenger')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(blank=True, choices=[(0, 'Bronze V'), (1, 'Bronze IV'), (2, 'Bronze III'), (3, 'Bronze II'), (4, 'Bronze I'), (5, 'Silver V'), (6, 'Silver IV'), (7, 'Silver III'), (8, 'Silver II'), (9, 'Silver I'), (10, 'Gold V'), (11, 'Gold IV'), (12, 'Gold III'), (13, 'Gold II'), (14, 'Gold I'), (15, 'Platinum V'), (16, 'Platinum IV '), (17, 'Platinum III'), (18, 'Platinum II'), (19, 'Platinum I'), (20, 'Diamond V'), (21, 'Diamond IV'), (22, 'Diamond III'), (23, 'Diamond II'), (24, 'Diamond I'), (25, 'Challenger')], null=True),
        ),
    ]
