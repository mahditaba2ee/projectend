# Generated by Django 4.0.5 on 2022-07-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_replaycommentmodel_created_replaycommentmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='replaycommentmodel',
            name='to_user',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
