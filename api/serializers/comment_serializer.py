from rest_framework.serializers import *
from ..models.comment_model import Comment


class CommentSerializer(ModelSerializer):
    comment_id = IntegerField(allow_null=True, required=False)
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user_id',
            'post_id',
            'comment_id',
            'message',
            'created_at',
            'updated_at',
            'deleted_at'
        ]