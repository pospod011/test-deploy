from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Не верный пароль или логин ")






class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age', 'director_image']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image']


class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['janre_name']



class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = '__all__'


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_image', 'movie_name', 'year']

class MovieDetailSerializer(serializers.ModelSerializer):
    movies = MovieLanguages()
    favorite_movie = FavoriteMovie()
    ratings = Rating()
    history_movie = History()
    movie_time = serializers.DateTimeField(format='%d-%h-%M')


    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor', 'janre', 'types', 'movie_time', 'description',
                  'movie_trailer', 'movie_image', 'status_movie', 'favorite_movie', 'ratings', 'movies', 'movie_moment',
                  'history_movie']


