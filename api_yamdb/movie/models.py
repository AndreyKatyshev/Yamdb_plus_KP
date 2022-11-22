from django.db import models


from reviews.models import (
    # Category,
    # Comment,
    Genre,
    GenreTitle,
    # Review,
    # Title,
)
# from users.models import User
from persons.models import Person


class Movie(models.Model):
    externalId = models.JSONField()
    logo = models.JSONField()
    poster = models.JSONField()
    backdrop = models.JSONField()
    rating = models.JSONField()
    votes = models.JSONField()
    videos = models.JSONField()
    budget = models.JSONField()
    fees = models.JSONField()
    distributors = models.JSONField()
    premiere = models.JSONField()
    images = models.JSONField()
    watchability = models.JSONField()
    collections = models.JSONField()
    updateDates = models.JSONField()
    status = models.JSONField()
    movieLength = models.JSONField()
    productionCompanies = models.JSONField()
    spokenLanguages = models.JSONField()
    id = models.IntegerField(unique=True,)
    type = models.CharField(max_length=100, verbose_name='Тип или категоря')
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Описание'
    )
    slogan = models.CharField(max_length=150, verbose_name='Слоган')
    year = models.DateField('Год выхода', db_index=True)
    facts = models.JSONField()
    genres = models.ManyToManyField(
        Genre,
        through=GenreTitle,
        related_name='movie',
        verbose_name='Жанр'
    )
    countries = models.JSONField()
    seasonsInfo = models.JSONField()
    persons = models.ManyToManyField(
        Person,
        related_name='movie',
        verbose_name='Люди'
    )
    lists = models.JSONField()
    typeNumber = models.FloatField()
    alternativeName = models.CharField(
        max_length=150, verbose_name='Альтернативное название')
    enName = models.JSONField()
    names = models.JSONField()
    sequelsAndPrequels = models.JSONField()
    updatedAt = models.DateTimeField()
    similarMovies = models.JSONField()
    ratingMpaa = models.CharField(
        max_length=150, null=True)
    shortDescription = models.CharField(
        max_length=150, null=True)
    technology = models.JSONField()
    ticketsOnSale = models.BooleanField()
    imagesInfo = models.JSONField()
    ageRating = models.CharField(
        max_length=150, null=True, verbose_name='Возрастной рейтинг')
    top10 = models.CharField(
        max_length=150, null=True, verbose_name='ТОП 10')
    top250 = models.CharField(
        max_length=150, null=True, verbose_name='ТОП 250')
    createDate = models.DateTimeField('Дата создания')
    releaseYears = models.DateField('Год релиза', db_index=True)
