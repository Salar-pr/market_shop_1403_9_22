# Generated by Django 5.1.3 on 2024-12-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_order', '0006_remove_userprofile_fax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='آدرس محل تحویل'),
        ),
    ]