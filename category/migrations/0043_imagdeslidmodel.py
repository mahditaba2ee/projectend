# Generated by Django 4.1 on 2022-09-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0042_alter_productmodel_like_alter_productmodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagdeSlidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
            ],
        ),
    ]