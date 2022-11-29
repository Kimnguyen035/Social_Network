from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..models.auth_model import *
from ..serializers.user_serializer import *
# from rest_framework.authtoken.models import Token

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class AuthView(ViewSet):
    def login(self, request):
        loginRequest = request.data.copy()
        user_name = loginRequest['username']
        try:
            get_user = User.objects.get(user_name=user_name)
        except:
            return Response("khong co du lieu")
        get_all_user = User.objects.filter()
        result = UserSerializer(get_all_user, many=True)
        return Response(result.data)

# Create your views here.
