# Generated by Django 3.2.15 on 2022-08-24 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0041_auto_20220823_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hasilreview',
            name='sudah_direview',
        ),
        migrations.AddField(
            model_name='hasilreview',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.statuspaketsoal'),
        ),
        migrations.AddField(
            model_name='soal_paketsoal',
            name='status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.statuspaketsoal'),
        ),
    ]
