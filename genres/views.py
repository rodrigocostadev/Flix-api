


# import json
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt # É comocado para não dar erro no envio do método POST

from genres.models import Genre
from rest_framework import generics # SEGURAR O CONTROL E CLICAR EM GENERICS PARA VER AS CLASSES PARA FAZER AS REQUISIÇÕES
from genres.serializers import GenreSerializer

# ////////////////////////////////////////////////////////
#//////////////    USANDO CBV     ////////////////////////

# Lista e cria dados da API
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): # Pega (Retrieve = pega), faz Update e Deleta (Destroy)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
    
    
    
    
    
# ////////////////////////////////////////////////////////
#//////////////    USANDO FBV     ////////////////////////

# Lista e cria
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET': # Retorna todos os generos que estão salvos no banco de dados da api
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
    
#     elif request.method == 'POST': # Envia os dados que alguem mandar por metodo POST para salvar no banco de dados
#         data = json.loads(request.body.decode('utf-8')) # decodificando em formato utf-8 (padrão de caracteres que aceita alguns caracteres especiais) / busca no body do post o genero que ele quer salvar
#         new_genre = Genre(name=data['name']) # dados que a api vai receber que foi mandado pelo metodo post
#         new_genre.save()
#         return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201) # Status 201 em protocolos http significa que foi criado um objeto novo na api
    
 
# # Pega os dados de um genero específico, altera e deleta
# @csrf_exempt   
# def genre_detail_view(request, pk):
#     # genre = Genre.objects.get(pk=pk)
#     genre = get_object_or_404(Genre, pk=pk)
    
#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name})
    
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message':'Genero excluído com sucesso!'}, status=204) # Quando deletar um objeto de uma api rest, o padrão é retornar um status 204