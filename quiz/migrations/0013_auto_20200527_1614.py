# Generated by Django 2.1.15 on 2020-05-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20200527_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paketsoal',
            old_name='id_creator',
            new_name='creator',
        ),
    ]