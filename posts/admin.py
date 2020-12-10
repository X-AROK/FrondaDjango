from django.contrib import admin
from .models import Post
from .models import Video
from .models import Studio
from .models import Dubber
from .models import Timer


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('upload_data',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass


@admin.register(Dubber)
class DubberAdmin(admin.ModelAdmin):
    pass


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    pass
