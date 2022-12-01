from rest_framework import serializers
from ..models.post_model import *
from ..configs.variable_response import *
from ..serializers.post_serializer import *

class IdValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, value):
        queryset = Post.objects.filter(id=value)
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['NOT_EXISTS_POST'])
        return value
    
class EditBlogValidate(IdValidate):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField()