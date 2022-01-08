from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('register/client/', RegisterClientView.as_view()),
    path('login/client/', LoginView.as_view()),

]