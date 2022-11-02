# Generated by Django 3.2.15 on 2022-08-23 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0039_paketsoal_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='HasilReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sudah_direview', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='peninjau',
            name='soal',
        ),
        migrations.AddField(
            model_name='peninjau',
            name='paket_soal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.paketsoal'),
        ),
    ]
