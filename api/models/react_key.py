from django.db import models
# from ..models.auth_model import User

class ReacKey(models.Model):
    class Meta:
        db_table = 'react_key'
    id = models.AutoField(primary_key=True)
    key = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()