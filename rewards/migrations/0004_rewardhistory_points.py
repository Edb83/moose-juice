# Generated by Django 3.2 on 2021-05-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0003_auto_20210514_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='rewardhistory',
            name='points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]