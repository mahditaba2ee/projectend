# Generated by Django 4.0.5 on 2022-08-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0019_categorymodel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
