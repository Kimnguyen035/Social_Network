from rest_framework.serializers import *
from ..models.auth_model import *

class UserSerializer(ModelSerializer):
    # id = IntegerField()
    username = CharField(source='user_name')
    # password = CharField()
    createdAt = DateTimeField(allow_null=True, required=False, source="created_at")
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "createdAt",
            "updated_at",
            "deleted_at"
        ]