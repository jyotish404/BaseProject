# Generated by Django 4.0 on 2021-12-19 02:30

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('team_member', '0003_auto_20210903_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
