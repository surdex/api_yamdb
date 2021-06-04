from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    USER_ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]
    username = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
    )
    confirmation_code = models.CharField(
        max_length=40,
        blank=True,
    )
    bio = models.TextField(
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=USER_ROLES,
        default='user'
    )
    password = models.CharField(
        max_length=128,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'password',
    ]

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email


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
    year = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(
        Genre, blank=True, related_name='titles'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='titles'
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.ForeignKey(
        'Title', on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=['author', 'title'],
                                    name='unique_review')
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    review = models.ForeignKey(
        'Review', on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text
