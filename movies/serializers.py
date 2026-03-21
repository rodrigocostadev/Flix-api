
from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
        
class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True) # Many = True, muitos atores para um filme
    genre = GenreSerializer() # Para exibir os dados do genero relacionado ao filme, utilizando o GenreSerializer para formatar a resposta
    rate = serializers.SerializerMethodField(read_only=True) # Campo calculado, não existe no model, por isso é um SerializerMethodField
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume'] # Campos que serão exibidos na resposta da API, incluindo o campo calculado 'rate'
        
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(avg_rate=Avg('stars'))['avg_rate'] # Calcula a média das avaliações (stars) dos reviews relacionados ao filme (obj)

        if rate:
            return round(rate, 2) # Arredonda a média para 2 casas decimais
        
        return None
        

class MovieStatsSerializer(serializers.Serializer): # Não é um model serializer, pois é um serualizer feito manualmente sem a utilização de metodos prontos
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField() # Lista de dicionarios com o nome do genero e a quantidade de filmes daquele genero
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()