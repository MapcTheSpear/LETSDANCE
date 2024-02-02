from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view),
    path('authorisation/', views.authorisation_api_view),
    path('confirm/', views.user_confirm_api_view),
]
