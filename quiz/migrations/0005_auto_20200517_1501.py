# Generated by Django 2.1.15 on 2020-05-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20200517_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statussoal',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
