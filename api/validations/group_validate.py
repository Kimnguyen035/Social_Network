from rest_framework.serializers import *
from ..models.group_model import Group
from ..configs.variable_response import *

class CheckInputValidate(Serializer):
    group_name = CharField(max_length=255)
    
class IdValidate(Serializer):
    id = IntegerField()
    
    def validate_id(self, value):
        if not Group.objects.filter(id=value).exists():
            raise ValidationError(ERROR['NOT_EXISTS_GROUP'])
        return value