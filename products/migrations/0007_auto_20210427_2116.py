# Generated by Django 3.2 on 2021-04-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='available_sizes',
            field=models.ManyToManyField(to='products.Size'),
        ),
    ]
