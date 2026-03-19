
from rest_framework import serializers
from movies.models import Movie

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        

class MovieStatsSerializer(serializers.Serializer): # Não é um model serializer, pois é um serualizer feito manualmente sem a utilização de metodos prontos
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField() # Lista de dicionarios com o nome do genero e a quantidade de filmes daquele genero
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()