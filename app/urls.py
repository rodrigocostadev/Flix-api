
from django.contrib import admin
from django.urls import path
# from genres.views import genre_create_list_view,genre_detail_view  # Usando FBV
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view() , name='genre-detail-view')
    
    # path('genres/', genre_create_list_view, name='genre-create-list'),
    # path('genres/<int:pk>/', genre_detail_view , name='genre-detail-view')
]
