from django.db import models
# from ..models.auth_model import User

class Group(models.Model):
    class Meta:
        db_table = 'group'
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    
class GroupUser(models.Model):
    class Meta:
        db_table = 'group_user'
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    group_id = models.BigIntegerField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()