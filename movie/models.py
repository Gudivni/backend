from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField()
    duration = models.IntegerField()
    release_year = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def filtered_review_list(self):
        return self.review_list.filter(stars__gt=3)

    @property
    def genres_list(self):
        return [genre.name for genre in self.genres.all()]


STAR_CHOICES = ((iterator_, '* ' * iterator_) for iterator_ in range(1, 6))


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='review_list')
    text = models.TextField()
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text
