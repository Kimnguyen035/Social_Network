from django.db import models

class Comment(models.Model):
    class Meta:
        db_table = 'comment'
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
    comment_id = models.BigIntegerField()
    message = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()