from django.db import models

# User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(
        Genre, blank=True, related_name='titles'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True,
        related_name='titles'
    )

    def __str__(self):
        return self.name

