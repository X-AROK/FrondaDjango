import datetime

from django.db import models
from category.models import Category
from category.models import Type
from category.models import Genre
from player.models import Player


class Studio(models.Model):
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'


class Dubber(models.Model):
    name = models.CharField("Имя", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Даббер'
        verbose_name_plural = 'Дабберы'


class Timer(models.Model):
    name = models.CharField("Имя", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таймер'
        verbose_name_plural = 'Таймеры'


class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    country = models.CharField("Страна", max_length=255)
    year = models.CharField("Год", max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, verbose_name="Студия", null=True)
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    voiced = models.ManyToManyField(Dubber, verbose_name="Роли озвучивали", null=True)
    timing = models.ManyToManyField(Timer, verbose_name="Тайминг и работа над звуком", null=True)
    description = models.TextField("Описание")
    img = models.ImageField(verbose_name="Обложка", upload_to='posts/imgs/')

    def __str__(self):
        return self.title

    def get_genres_str(self):
        result = self.genres.order_by('name')
        genres = [str(genre) for genre in result]
        return ", ".join(genres)

    def get_voiced_str(self):
        result = self.voiced.order_by('name')
        voiced = [str(dubber) for dubber in result]
        return ", ".join(voiced)

    def get_timing_str(self):
        result = self.timing.order_by('name')
        timing = [str(timer) for timer in result]
        return ", ".join(timing)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Video(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Плеер")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    season = models.IntegerField("Сезон")
    episode = models.IntegerField("Серия")
    url = models.URLField("Ссылка")
    upload_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.post.title} [{self.player.name}] ({self.season} - {self.episode})'

    class Meta:
        ordering = ('post__title', 'player__name', 'season', 'episode')
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
