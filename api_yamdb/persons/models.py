from django.db import models

from movie.models import Movie


class Person(models.Model):
    spouses = models.JSONField()
    id = models.IntegerField()
    __v = models.IntegerField()
    age = models.IntegerField(verbose_name='Возраст')
    birthPlace = models.JSONField(verbose_name='Место Рождения')
    birthday = models.DateTimeField(verbose_name='День Рождения')
    countAwards = models.JSONField()
    createdAt = models.DateTimeField()
    death = models.CharField(
        max_length=50, null=True)
    deathPlace = models.JSONField()
    enName = models.CharField(
        max_length=100, verbose_name='Имя по Английски')
    facts = models.JSONField()
    growth = models.IntegerField(verbose_name='Рост')
    movies = models.ManyToManyField(
        Movie,
        related_name='persons',
        verbose_name='Картины'
    )
    name = models.CharField(
        max_length=100, verbose_name='Имя')
    photo = models.URLField()
    profession = models.JSONField()
    sex = models.CharField(
        max_length=50, verbose_name='Пол')
    updatedAt = models.DateTimeField()
