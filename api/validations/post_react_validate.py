from rest_framework.serializers import *
from ..models.post_model import PostReact
from ..models.auth_model import User
from ..models.post_model import Post
from ..models.react_key import ReacKey
from ..configs.variable_response import *

class IdPostReactValidate(Serializer):
    id = IntegerField(required=True)
    
    def validate_id(self, value):
        if not PostReact.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_POST_REACT'])
        return value
    
class PostReactValidate(Serializer):
    user_id = IntegerField()
    post_id = IntegerField()
    react = IntegerField()
    
    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_USER_ID'])
        return value
    
    def validate_post_id(self, value):
        if not Post.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_POST_ID'])
        return value
    
    def validate_react(self, value):
        if not ReacKey.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_REACT'])
        return value