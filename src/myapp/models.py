from django.db import models
from myapp.utils import text_lat

class Citi(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name = 'Введите название города',
                            unique=True)
    
    slug = models.CharField(max_length=50, blank=True, unique=False)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Название городов'
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text_lat(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык программирования',
                            unique=True)

    slug = models.CharField(max_length=50, blank=True, unique=False)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = text_lat(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=300,
                             verbose_name='Оглавление вакансии')
    company = models.CharField(max_length=300, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    timestamp = models.TimeField(auto_now_add=True)
    citi = models.ForeignKey(Citi, on_delete=models.CASCADE,
                             verbose_name='Город')
    language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                 verbose_name='Язык программирования')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title