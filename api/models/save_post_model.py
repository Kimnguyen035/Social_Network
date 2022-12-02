from django.db import models


class SavePost(models.Model):
    class Meta:
        db_table = 'save_post'
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    post_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()