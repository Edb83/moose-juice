# Generated by Django 3.2 on 2021-04-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210427_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='nicotine',
            name='type',
            field=models.CharField(blank=True, choices=[('freebase', 'FREEBASE'), ('salt', 'SALT')], max_length=8, null=True),
        ),
    ]