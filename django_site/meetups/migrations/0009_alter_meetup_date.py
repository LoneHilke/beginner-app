# Generated by Django 4.0.4 on 2022-04-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0008_alter_meetup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='date',
            field=models.DateField(),
        ),
    ]
