
from django.contrib import admin
from django.urls import path, include
# from genres.views import genre_create_list_view,genre_detail_view  # Usando FBV

# from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
# from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
# from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
# from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    
    # path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    # path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view() , name='genre-detail-view'),
    
    # path('actors/', ActorCreateListView.as_view(), name="actor-create-list"),
    # path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name="actor-detail-view"),
    
    # path('movies/', MovieCreateListView.as_view(),name="movie-create-list"),
    # path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(),name="move-detail-view"),
    
    # path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    # path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
    
    # path('genres/', genre_create_list_view, name='genre-create-list'),
    # path('genres/<int:pk>/', genre_detail_view , name='genre-detail-view')
]
