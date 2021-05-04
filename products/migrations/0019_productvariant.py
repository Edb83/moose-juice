# Generated by Django 3.2 on 2021-05-04 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20210501_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('nicotine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.nicotine')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
        ),
    ]