# Generated by Django 2.1 on 2018-08-16 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schooler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='number_of_students',
            new_name='max_students',
        ),
    ]
