# Generated by Django 3.2 on 2021-04-27 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_nicotine_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nicotine',
            old_name='friendly_name',
            new_name='strength',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='friendly_name',
            new_name='label',
        ),
        migrations.RemoveField(
            model_name='nicotine',
            name='name',
        ),
        migrations.RemoveField(
            model_name='size',
            name='name',
        ),
    ]
