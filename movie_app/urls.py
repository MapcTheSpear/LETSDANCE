from django.urls import path
from . import views
from .constants import LIST_CREATE, ITEM

urlpatterns = [
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movie/', views.MovieListCreateAPIView.as_view()),
    path('movie/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]