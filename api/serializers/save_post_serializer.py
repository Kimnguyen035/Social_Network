from rest_framework.serializers import *
from ..models.save_post_model import SavePost


class SavePostSerializer(ModelSerializer):
    created_at = DateTimeField(allow_null=True, required=False)
    updated_at = DateTimeField(allow_null=True, required=False)
    deleted_at = DateTimeField(allow_null=True, required=False)
    class Meta:
        model = SavePost
        fields = [
            'id',
            'user_id',
            'post_id',
            'created_at',
            'updated_at',
            'deleted_at'
        ]