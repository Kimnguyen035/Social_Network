from django.db import models
# from ..models.auth_model import User

class Post(models.Model):
    class Meta:
        db_table = "post"
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.BigIntegerField()
    group_id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    
class PostReact(models.Model):
    class Meta:
        db_table = "post_react"
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
    react = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()