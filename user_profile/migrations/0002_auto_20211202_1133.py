# Generated by Django 3.2.9 on 2021-12-02 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='row_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='row_last_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]