from django.contrib import admin
from .models import Category
from .models import Type
from .models import Genre


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
