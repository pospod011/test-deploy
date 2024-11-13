from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'movie', MovieListViewSet, basename='movie_list')
router.register(r'detail', MovieDetailViewSet, basename='movie_detail')
router.register(r'users', ProfileViewSet, basename='user_list')
router.register(r'review', RatingViewSet, basename='reviews')



urlpatterns = [
    path('', include(router.urls))

]