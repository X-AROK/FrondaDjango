# Generated by Django 3.1.2 on 2020-12-09 20:55

from django.db import migrations


def link_timing(apps, schema_editor):
    Timer = apps.get_model('posts', 'Timer')
    Post = apps.get_model('posts', 'Post')
    for post in Post.objects.all():
        names = post.timing.split(", ")
        for name in names:
            timing, created = Timer.objects.get_or_create(name=name)
            post.timing_link.add(timing)
        post.save()


def unlink_timing(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    for post in Post.objects.all():
        result = post.timing_link.order_by('name')
        timing = [str(timer) for timer in result]
        post.timing = ", ".join(timing)
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_transfer_voiced'),
    ]

    operations = [
        migrations.RunPython(link_timing, unlink_timing)
    ]
