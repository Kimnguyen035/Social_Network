from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..helper.response import *
from datetime import datetime

from ..models.group_model import Group

from ..serializers.group_serializer import *

from ..validations.group_validate import *

class GroupView(ViewSet):

    def get_all_group(self, request):
        data = request.GET.copy()
        queryset = Group.objects.filter(deleted_at=None)
        group = GroupSerializer(queryset, many=True)
        return response_data(data=group.data)
    
    def detail_group(self, request, id):
        data = request.GET.copy()
        queryset = Group.objects.filter(id=id)
        if not queryset.exists():
            return response_data(message=ERROR('NOT_EXISTS_GROUP'),status=STATUS('NO_DATA'))
        group_save = GroupSerializer(queryset,many=True)
        return response_data(data=group_save.data[0])
    
    def add_group(self, request):
        data = request.data.copy()
        validate = CheckInputValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors,status=STATUS['NO_DATA'])
        group_save = GroupSerializer(data=validate.data)
        if not group_save.is_valid():
            return validate_error(group_save.errors,status=STATUS['FAIL_REQUEST'])
        group_save.save()
        return response_data(message=SUCCESS['ADD_GROUP'], data=group_save.data)
    
    def delete_group(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,status=STATUS['NO_DATA'])
        group_save = Group.objects.get(id=validate.data)
        group_save.deleted_at = datetime.now()
        group_save.save()
        serializer = GroupSerializer(group_save)
        return response_data(message=SUCCESS['DELETE_GROUP'], data=serializer.data)