# Generated by Django 2.1.15 on 2020-05-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_paketsoal_generate_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paketsoal',
            name='generate_date',
        ),
        migrations.AddField(
            model_name='indikator_user',
            name='is_done',
            field=models.BooleanField(default=0),
        ),
    ]
