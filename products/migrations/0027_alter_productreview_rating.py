# Generated by Django 3.2 on 2021-05-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_productreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=4),
        ),
    ]