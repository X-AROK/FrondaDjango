# Generated by Django 3.1.2 on 2020-12-09 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20201209_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timing_link',
        ),
        migrations.AddField(
            model_name='post',
            name='timing_link',
            field=models.ManyToManyField(null=True, to='posts.Timer', verbose_name='Тайминг и работа над звуком'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='voiced_link',
        ),
        migrations.AddField(
            model_name='post',
            name='voiced_link',
            field=models.ManyToManyField(null=True, to='posts.Dubber', verbose_name='Роли озвучивали'),
        ),
    ]
