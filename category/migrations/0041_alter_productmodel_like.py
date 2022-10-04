# Generated by Django 4.1 on 2022-09-03 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0040_alter_productmodel_like_alter_productmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
