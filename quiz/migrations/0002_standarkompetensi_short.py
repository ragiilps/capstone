# Generated by Django 2.1.15 on 2020-05-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standarkompetensi',
            name='short',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
