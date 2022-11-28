from django.contrib import admin
from django.urls import path
from .Views.auth_view import AuthView

urlpatterns = [
    path('', AuthView.as_view({"get":"login"})),
]
