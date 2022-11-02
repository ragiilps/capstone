# Generated by Django 4.0.4 on 2022-09-07 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0039_templatesoal_id_user_delete_templatesoal2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatesoal',
            name='id_user',
        ),
        migrations.CreateModel(
            name='TemplateSoal2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.TextField()),
                ('soal', tinymce.models.HTMLField(null=True)),
                ('variasi', models.IntegerField()),
                ('pengacakan', models.CharField(max_length=20)),
                ('var1', tinymce.models.HTMLField()),
                ('variabel', tinymce.models.HTMLField()),
                ('rumus', models.TextField()),
                ('jawaban', tinymce.models.HTMLField(null=True)),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
