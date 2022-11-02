# Generated by Django 2.1.15 on 2021-06-20 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_merge_20210620_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matakuliah',
            name='SO',
        ),
        migrations.AddField(
            model_name='studentoutcome',
            name='matkul',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.MataKuliah'),
        ),
        migrations.AlterField(
            model_name='learningoutcome',
            name='SO',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.StudentOutcome'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='matkul',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.MataKuliah'),
        ),
    ]
