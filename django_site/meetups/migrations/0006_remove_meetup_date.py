# Generated by Django 4.0.4 on 2022-04-21 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_meetup_date_meetup_organizer_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='date',
        ),
    ]
