from rest_framework import serializers
from . models import Movies, Collection, Genres

class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ['id','title' , 'description','uuid']

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id'  , 'title' , 'description' , 'uuid']

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','genre','movie']