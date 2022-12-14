# Generated by Django 4.1 on 2022-08-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0025_alter_brandmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='typeproductmodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='آدرس لینک'),
        ),
    ]
