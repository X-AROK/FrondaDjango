from django.db import models


class Slider(models.Model):
    alt = models.CharField("Название", max_length=255)
    url = models.URLField("Ссылка")
    img = models.ImageField(verbose_name="Изображение", upload_to='sliders/imgs/')

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
