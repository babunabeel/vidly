# Generated by Django 3.0.3 on 2020-02-10 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 10, 12, 29, 14, 68871, tzinfo=utc)),
        ),
    ]