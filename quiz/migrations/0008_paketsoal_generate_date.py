# Generated by Django 2.1.15 on 2020-05-17 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_revisisoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='paketsoal',
            name='generate_date',
            field=models.DateTimeField(null=True),
        ),
    ]
