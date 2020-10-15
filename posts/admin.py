from django.contrib import admin
from .models import Post
from .models import Video


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('upload_data',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
