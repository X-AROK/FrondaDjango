from django.db import models


class MenuItem(models.Model):
    title = models.CharField("Название", max_length=255)
    url = models.CharField("Локальная ссылка", max_length=255)
    position = models.IntegerField("Позиция в меню", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('position', )
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"
