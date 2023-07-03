# Generated by Django 4.2.2 on 2023-07-03 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterMarkRemove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/')),
                ('sdate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
