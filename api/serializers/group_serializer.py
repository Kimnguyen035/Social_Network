from rest_framework.serializers import *
from ..models.group_model import Group


class GroupSerializer(ModelSerializer):
    group_name = CharField(allow_null=True, required=False)
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = Group
        fields = [
            'id',
            'group_name',
            'created_at',
            'updated_at',
            'deleted_at'
        ]