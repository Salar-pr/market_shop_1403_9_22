# Generated by Django 4.2 on 2025-01-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='galleries'),
        ),
    ]