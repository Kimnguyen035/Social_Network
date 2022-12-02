from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class AuthView(ViewSet):
    def login(self, request):
        return Response()