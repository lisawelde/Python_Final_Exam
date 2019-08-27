# Generated by Django 2.2.3 on 2019-08-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190825_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='users_trips',
        ),
        migrations.AddField(
            model_name='trip',
            name='users_who_join',
            field=models.ManyToManyField(related_name='joined_trips', to='myapp.User'),
        ),
    ]
