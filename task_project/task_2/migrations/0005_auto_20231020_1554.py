# Generated by Django 2.2 on 2023-10-20 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_2', '0004_auto_20231020_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='note-text',
            new_name='note_text',
        ),
    ]
