# Generated by Django 5.1.1 on 2024-12-07 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_order', '0004_remove_order_item_alter_order_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='آدرس ایمیل')),
                ('phone_number', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('fax', models.CharField(blank=True, max_length=50, null=True, verbose_name='فکس')),
                ('address', models.CharField(max_length=255, verbose_name='آدرس محل تحویل')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('postcode', models.CharField(max_length=20, verbose_name='کد پستی')),
                ('card_number', models.CharField(max_length=16, verbose_name='شماره کارت')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]