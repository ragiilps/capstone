# Generated by Django 2.1.15 on 2020-06-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20200530_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='golongan',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='profile',
            name='jabatan',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='nip',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='nomer_hp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='pangkat',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
