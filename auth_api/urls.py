from django.contrib import admin
from django.urls import path
from .views.auth_view import AuthView
from .views.token_view import *


urlpatterns = [
    path('', AuthView.as_view({"get":"login"})),
    path('api/token/', CustomAuthToken.as_view()),
]
