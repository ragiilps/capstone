# Generated by Django 3.2.15 on 2022-08-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0036_merge_0025_peninjau_0035_auto_20220801_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='paketsoal',
            name='semester',
            field=models.CharField(default='Gasal', max_length=7),
        ),
        migrations.AddField(
            model_name='paketsoal',
            name='tahun_ajaran',
            field=models.IntegerField(default=2016),
        ),
    ]
