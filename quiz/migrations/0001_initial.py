# Generated by Django 2.1.15 on 2021-05-26 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_soal', models.TextField()),
                ('generated_option', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indikator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('deskripsi', models.TextField()),
                ('level_kognitif', models.CharField(max_length=20)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Indikator_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KompetensiDasar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LearningOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LO', models.CharField(blank=True, max_length=200)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matkul', models.TextField()),
                ('kode_matkul', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.IntegerField(default=None)),
                ('deskripsi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaketSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField()),
                ('judul', models.TextField()),
                ('jumlah_paket', models.IntegerField()),
                ('is_generated', models.BooleanField(null=True)),
                ('generated_date', models.DateTimeField(null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Penugasan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurikulum', models.CharField(blank=True, max_length=200)),
                ('created_date', models.DateTimeField(null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('learning_outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.LearningOutcome')),
                ('mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MataKuliah')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sekolah', models.CharField(blank=True, max_length=100)),
                ('alamat', models.CharField(blank=True, max_length=200)),
                ('mapel', models.CharField(blank=True, max_length=20)),
                ('nomer_hp', models.CharField(blank=True, max_length=20)),
                ('jabatan', models.CharField(blank=True, max_length=100)),
                ('nip', models.CharField(blank=True, max_length=30)),
                ('golongan', models.CharField(blank=True, max_length=4)),
                ('pangkat', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RevisiSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.TextField()),
                ('soal', models.TextField()),
                ('variasi', models.IntegerField()),
                ('pengacakan', models.CharField(max_length=20)),
                ('var1', models.CharField(max_length=100)),
                ('variabel', models.TextField()),
                ('rumus', models.TextField()),
                ('jawaban', models.TextField()),
                ('variabel_gambar', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=None)),
                ('id_creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('indikator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.Penugasan')),
            ],
        ),
        migrations.CreateModel(
            name='Soal_PaketSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer_urut', models.IntegerField(null=True)),
                ('nomer_paket', models.IntegerField(null=True)),
                ('generated_soal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.GeneratedSoal')),
                ('paket_soal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.PaketSoal')),
            ],
        ),
        migrations.CreateModel(
            name='StandarKompetensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurikulum', models.IntegerField()),
                ('kelas', models.IntegerField()),
                ('deskripsi', models.TextField()),
                ('tipe', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SO', models.CharField(blank=True, max_length=200)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TemplateSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.TextField()),
                ('soal', models.TextField()),
                ('variasi', models.IntegerField()),
                ('pengacakan', models.CharField(max_length=20)),
                ('var1', models.CharField(max_length=20)),
                ('variabel', models.TextField()),
                ('rumus', models.TextField()),
                ('jawaban', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topik', models.TextField(null=True)),
                ('matkul', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.MataKuliah')),
            ],
        ),
        migrations.AddField(
            model_name='soal',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.StatusSoal'),
        ),
        migrations.AddField(
            model_name='revisisoal',
            name='soal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Soal'),
        ),
        migrations.AddField(
            model_name='penugasan',
            name='student_outcome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.StudentOutcome'),
        ),
        migrations.AddField(
            model_name='penugasan',
            name='topik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Topic'),
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='SO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.StudentOutcome'),
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='SO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.StudentOutcome'),
        ),
        migrations.AddField(
            model_name='kompetensidasar',
            name='StandarKompetensi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.StandarKompetensi'),
        ),
        migrations.AddField(
            model_name='kompetensidasar',
            name='materi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Materi'),
        ),
        migrations.AddField(
            model_name='indikator_user',
            name='indikator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Penugasan'),
        ),
        migrations.AddField(
            model_name='indikator_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='indikator',
            name='kompetensi_dasar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.KompetensiDasar'),
        ),
        migrations.AddField(
            model_name='generatedsoal',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.Soal'),
        ),
    ]
