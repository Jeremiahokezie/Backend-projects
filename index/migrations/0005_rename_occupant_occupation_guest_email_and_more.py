# Generated by Django 4.0.4 on 2022-06-15 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_guest_number_of_nights_alter_guest_room_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='Occupant_Occupation',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='Occupant_Name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='Occupant_Email',
            new_name='Occupation',
        ),
    ]
