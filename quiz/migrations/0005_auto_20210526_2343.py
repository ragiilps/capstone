# Generated by Django 2.1.15 on 2021-05-26 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210526_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soal',
            old_name='penugasan',
            new_name='indikator',
        ),
    ]
