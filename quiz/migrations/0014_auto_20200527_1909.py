# Generated by Django 2.1.15 on 2020-05-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20200527_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paketsoal',
            name='judul',
            field=models.TextField(),
        ),
    ]
