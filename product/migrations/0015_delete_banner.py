# Generated by Django 5.1.3 on 2024-12-10 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_banner_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
    ]