# Generated by Django 5.1.1 on 2024-11-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='ترتیب'),
        ),
    ]
