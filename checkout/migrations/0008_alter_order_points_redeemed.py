# Generated by Django 3.2 on 2021-05-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='points_redeemed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
