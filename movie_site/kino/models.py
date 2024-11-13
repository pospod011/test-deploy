from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(18),
                                                                              MaxValueValidator(90)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=22, unique=True)

    def __str__(self):
        return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=22)
    bio = models.TextField()
    age = models.PositiveIntegerField(default=0)
    director_image = models.ImageField(upload_to='director_images/', null=True, blank=True)

    def __str__(self):
        return self.director_name
class Actor(models.Model):
    actor_name = models.CharField(max_length=22)
    bio = models.TextField()
    age = models.PositiveIntegerField(default=0)
    actor_image = models.ImageField(upload_to='actor_images/', null=True, blank=True)

    def __str__(self):
        return self.actor_name

class Janre(models.Model):
    janre_name = models.CharField(max_length=22, unique=True)

    def __str__(self):
        return self.janre_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=88)
    year = models.DateField()
    country = models.ManyToManyField(Country, related_name='country_movie')
    director = models.ManyToManyField(Director, related_name='director_movie')
    actor = models.ManyToManyField(Actor, related_name='actor_movie')
    janre = models.ManyToManyField(Janre, related_name='janre_movie')

    TYPES_CHOICES = (
        ('1080', '1080'),
        ('720', '720'),
        ('480', '480'),
        ('360', '360'),
        ('144', '144'),

    )

    types = MultiSelectField(max_length=11, choices=TYPES_CHOICES, max_choices=5)
    movie_time = models.DateTimeField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/', null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_image/', null=True, blank=True)

    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple'),

    )

    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.movie_name

class MovieLanguages(models.Model):
    language = models.CharField(max_length=12)
    video = models.FileField(upload_to='vid/', null=True, blank=True)
    movie = models.ForeignKey(Movie, related_name='movies', on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_moment', on_delete=models.CASCADE)
    movie_moments = models.ImageField(upload_to='movie_moment/', null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(Profile, related_name='rating_user', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name="RATING")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie} - {self.user} - {self.stars} stars"


class Favorite(models.Model):
    user = models.OneToOneField(Profile, related_name='favorite_user', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.user}

class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name='cart', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='favorite_movie', on_delete=models.CASCADE)

class History(models.Model):
    user = models.ForeignKey(Profile, related_name='history_user', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='history_movie', on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)



