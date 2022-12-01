
from rest_framework.serializers import *
from ..models.auth_model import User


class PostSerializer(ModelSerializer):
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'created_at',
            'updated_at',
            'deleted_at'
        ]