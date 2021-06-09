# Generated by Django 3.2.4 on 2021-06-09 08:52

from django.db import migrations
from django.contrib.auth.hashers import make_password


def createsuperuser(apps, schema_editor):
    User = apps.get_model('user', 'User')
    User.objects.create(
        username="admin",
        first_name="John",
        last_name="Doe",
        is_staff=True,
        is_superuser=True,
        password=make_password("test12345"),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            createsuperuser,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
