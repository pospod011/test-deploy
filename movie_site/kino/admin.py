from django.contrib import admin
from .models import *

class MovieLanguagesInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1



class MovieMomentsInline(admin.TabularInline):
    model = Moments
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguagesInline, MovieMomentsInline]


    class Media:



        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Movie, MovieAdmin)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Janre)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)

