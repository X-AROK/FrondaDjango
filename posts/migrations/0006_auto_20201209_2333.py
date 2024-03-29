# Generated by Django 3.1.2 on 2020-12-09 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20201014_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dubber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Даббер',
                'verbose_name_plural': 'Дабберы',
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Студия',
                'verbose_name_plural': 'Студии',
            },
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Таймер',
                'verbose_name_plural': 'Таймеры',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('post__title', 'player__name', 'season', 'episode'), 'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AddField(
            model_name='post',
            name='studio_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.studio', verbose_name='Студия'),
        ),
        migrations.AddField(
            model_name='post',
            name='timing_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.timer', verbose_name='Тайминг и работа над звуком'),
        ),
        migrations.AddField(
            model_name='post',
            name='voiced_link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.dubber', verbose_name='Роли озвучивали'),
        ),
    ]
