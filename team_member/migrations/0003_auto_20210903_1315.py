# Generated by Django 3.2.5 on 2021-09-03 19:15

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('team_member', '0002_teammember_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='admin_role',
            field=models.BooleanField(choices=[(False, "Regular - Can't delete team members"), (True, 'Admin - Can delete team members')], default=False),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='last_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
