from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..models.post_model import Post
from ..serializers.post_serializer import *
from datetime import datetime

class PostView(ViewSet):
    def get_all_post(self, request):
        posts = Post.objects.filter(deleted_at=None)
        result = PostSerializer(posts, many=True)
        return Response(result.data)
    
    def post_article(self, request):
        data = request.data.copy()
        postsave = PostSerializer(data=data)
        if not postsave.is_valid():
            return Response(post.errors)
        # luu bai viet vao mysql
        postsave.save()
        post = Post.objects.filter(id=postsave.data['id'])
        if not post.exists():
            return Response("Error")
        # dang bai viet
        post_detail = PostSerializer(post, many=True)
        return Response(post_detail.data)
    
    def get_post_detail(self, request):
        data = request.GET.copy()
        post = Post.objects.filter(id=data['id'])
        if not post.exists():
            return Response("Error")
        # xem chi tiet bai viet
        post_detail = PostSerializer(post, many=True)
        return Response(post_detail.data[0])
    
    def post_delete_soft(self,request):
        data = request.GET.copy()
        post = Post.objects.filter(id=data['id'])
        if not post.exists():
            return Response("Error")
        post_detail = PostSerializer(post, many=True)
        post_detail.data[0]['deleted_at'] = datetime.now()
        post_delete = PostSerializer(post_detail.data[0],many=True)
        post_delete.save()
        return Response()
