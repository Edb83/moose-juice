# Generated by Django 3.2 on 2021-05-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
