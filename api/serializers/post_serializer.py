from rest_framework.serializers import *
from ..models.post_model import Post


class PostSerializer(ModelSerializer):
    user_id = IntegerField(allow_null=True, required=False)
    group_id = IntegerField(allow_null=True, required=False)
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = Post
        fields = [
            'id',
            'user_id',
            'group_id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'deleted_at'
        ]