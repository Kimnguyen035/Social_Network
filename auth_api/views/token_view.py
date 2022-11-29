from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from ..models.auth_model import *
from ..serializers.user_serializer import *

class CustomAuthToken(ObtainAuthToken):

    def post(self, request):
        data = request.data.copy()
        try:
            user = User.objects.get(user_name = data['username'])
            u = {
                "username": user.user_name,
                "password": user.password
            }
        except:
            return Response("Error")
        token = Token.objects.create(user=u)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })