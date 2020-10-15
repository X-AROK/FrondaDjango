from django.db import models
from category.models import Category
from category.models import Type
from category.models import Genre
from player.models import Player


class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    country = models.CharField("Страна", max_length=255)
    year = models.CharField("Год", max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    studio = models.CharField("Студия", max_length=255)
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    voiced = models.TextField("Роли озвучивали")
    timing = models.TextField("Тайминг и работа над звуком")
    description = models.TextField("Описание")
    img = models.ImageField(verbose_name="Обложка", upload_to='posts/imgs/')

    def __str__(self):
        return self.title

    def get_genres_str(self):
        result = self.genres.order_by('name')
        genres = [str(genre) for genre in result]
        return ", ".join(genres)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Video(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Плеер")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    season = models.IntegerField("Сезон")
    episode = models.IntegerField("Серия")
    url = models.URLField("Ссылка")

    def __str__(self):
        return f'{self.post.title} ({self.season} - {self.episode})'

    class Meta:
        ordering = ('post__title', 'player__name', 'season', 'episode')
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
