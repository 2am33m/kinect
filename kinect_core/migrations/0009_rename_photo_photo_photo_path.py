# Generated by Django 4.2.6 on 2024-07-01 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinect_core', '0008_rename_photo_path_photo_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='photo_path',
        ),
    ]
