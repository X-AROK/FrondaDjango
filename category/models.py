from django.db import models


class Category(models.Model):
    name = models.CharField("Уникальное название", unique=True, max_length=255)
    display_name = models.CharField("Отображаемое название", max_length=255)
    show_on_homepage = models.BooleanField("Отображать на главной", default=True)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Type(models.Model):
    name = models.CharField("Название", unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Genre(models.Model):
    name = models.CharField("Название", unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
