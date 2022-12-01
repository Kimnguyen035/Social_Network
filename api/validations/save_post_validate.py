from rest_framework.serializers import *
from ..models.save_post_model import SavePost
from ..models.post_model import Post
from ..models.auth_model import User
from ..serializers.post_serializer import *
from ..configs.variable_response import *

class IdSavePostValidate(Serializer):
    id = IntegerField()
    
    def validate_id(self, value):
        if not SavePost.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_SAVE_POST'])
        return value
    
class SavePostValidate(Serializer):
    user_id = IntegerField()
    post_id = IntegerField()
    
    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_USER_ID'])
        return value
    
    def validate_post_id(self, value):
        if not Post.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_POST_ID'])
        return value