# Generated by Django 4.0.4 on 2022-07-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0032_alter_templatesoal_variabel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatesoal',
            name='var1',
            field=models.CharField(max_length=255),
        ),
    ]
