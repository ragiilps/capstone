# Generated by Django 4.0.4 on 2022-09-07 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0040_remove_templatesoal_id_user_templatesoal2'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatesoal',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TemplateSoal2',
        ),
    ]
