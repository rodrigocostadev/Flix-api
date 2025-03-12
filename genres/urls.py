from django.urls import path
from .import views # Importa todas as views de genero para esse arquivo
# from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view() , name='genre-detail-view'),
]









