# Generated by Django 5.0 on 2023-12-28 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='bonus',
        ),
    ]
