# Generated by Django 4.1 on 2022-09-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0029_alter_typeproductmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeproductmodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, unique=True, verbose_name='آدرس لینک'),
        ),
    ]
