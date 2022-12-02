from rest_framework.serializers import *
from ..models.post_react_model import PostReact


class PostReactSerializer(ModelSerializer):
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = PostReact
        fields = [
            'id',
            'user_id',
            'post_id',
            'react',
            'created_at',
            'updated_at',
            'deleted_at'
        ]