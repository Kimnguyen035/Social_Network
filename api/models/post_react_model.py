from django.db import models


    
class PostReact(models.Model):
    class Meta:
        db_table = 'post_react'
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
    react = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()