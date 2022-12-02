from rest_framework.serializers import *
from ..models.comment_model import Comment
from ..models.auth_model import User
from ..models.post_model import Post
from ..configs.variable_response import *
from ..serializers.comment_serializer import *

class CheckInputValidate(Serializer):
    user_id = IntegerField()
    post_id = IntegerField()
    message = CharField()
    comment_id = IntegerField(allow_null=True)
    
    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_USER_ID'])
        return value
    
    def validate_post_id(self, value):
        if not Post.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_POST_ID'])
        return value
    
    def validate_comment_id(self, value):
        if value is None:
            return value
        if not Comment.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_COMMENT'])
        return value
    
class IdCommentValidate(Serializer):
    id = IntegerField()
    
    def validate_id(self, value):
        if not Comment.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_COMMENT'])
        return value