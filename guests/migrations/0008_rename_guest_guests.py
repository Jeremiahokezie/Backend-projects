# Generated by Django 4.0.4 on 2022-06-16 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0007_alter_guest_room_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Guest',
            new_name='Guests',
        ),
    ]
