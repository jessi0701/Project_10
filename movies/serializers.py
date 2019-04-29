from rest_framework import serializers
from .models import Genre,Movie,Score

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
        
        
class GenreDetailSerializers(serializers.ModelSerializer):
    movies = MovieSerializers(source='movie_set', many=True)
    class Meta:
        model = Genre
        fields = ['id','name','movies']
        
class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id','content','value']
        