from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.directors_api_view),
    path('directors/<int:id>/', views.director_detail_api_view),
    path('movie/', views.movie_api_view),
    path('movie/<int:id>', views.movie_detail_api_view),
    path('reviews/', views.reviews_api_view),
    path('reviews/<int:id>', views.reviews_detail_api_view),
]