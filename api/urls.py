from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    #user
    path('register/client/', RegisterClientView.as_view()),
    path('login/client/', LoginView.as_view()),
    path('logout/client/', LogoutView.as_view()),
    #pokemon
    path('pokemon/create/', CreatePokemonView.as_view()),
    path('pokemon/list/', ListPokemonView.as_view()),
    path('pokemon/update/<int:pk>/', UpdatePokemonView.as_view()),
    path('pokemon/delete/<int:pk>/', DeletePokemonView.as_view()),
]