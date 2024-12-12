# Generated by Django 5.1.1 on 2024-11-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='sliders', verbose_name='عکس')),
                ('link', models.URLField()),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'اسلاید',
                'verbose_name_plural': 'اسلاید ها',
                'ordering': ['order'],
            },
        ),
    ]