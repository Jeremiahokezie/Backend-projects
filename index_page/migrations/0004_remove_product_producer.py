# Generated by Django 4.0.4 on 2022-06-04 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0003_alter_bio_name_of_family'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Producer',
        ),
    ]