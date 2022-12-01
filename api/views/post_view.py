from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ..serializers.post_serializer import *
from ..serializers.save_post_serializer import *
from ..validations.post_validate import *
from ..validations.save_post_validate import *
from ..validations.post_react_validate import *
from ..helper.response import *
from datetime import datetime

class PostView(ViewSet):
    def all_post(self, request):
        posts = Post.objects.filter(deleted_at=None)
        result = PostSerializer(posts, many=True)
        return response_data(result.data)
    
    def detail_post(self, request, id):
        data = request.GET.copy()
        post = Post.objects.filter(id=id)
        if not post.exists():
            return response_data(message=ERROR['NOT_EXISTS_POST'])
        post_detail = PostSerializer(post, many=True)
        return response_data(post_detail.data[0])
    
    def post_blog(self, request):
        data = request.data.copy()
        post_save = PostSerializer(data=data)
        if not post_save.is_valid():
            return response_data(message=post_save.errors, status=STATUS['NO_DATA'])
        post_save.save()
        return response_data(message=SUCCESS['POST_BLOG'],data=post_save.data)
    
    def edit_post(self, request, id):
        data = request.data.copy()
        data['id'] = id
        validate = EditBlogValidate(data=data)
        if not validate.is_valid():
            return response_data(message=validate.errors, status=STATUS['NO_DATA'])
        queryset = Post.objects.get(id=validate.data['id'])
        data_save = PostSerializer(queryset, data=data)
        if not data_save.is_valid():
            return response_data(message=data_save.errors, status=STATUS['FAIL_REQUEST'])
        data_save.save()
        return response_data(message=SUCCESS['EDIT_POST'],data=data_save.data)
    
    def delete_post(self,request,id):
        data = request.GET.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return response_data(message=validate.errors,status=STATUS['NO_DATA'])
        result = Post.objects.get(id=validate.data['id'])
        result.deleted_at = datetime.now()
        result.save()
        serializer = PostSerializer(result)
        return response_data(message=SUCCESS['DELETED_POST'],data=serializer.data)
    
    def get_trash(self, request):
        data = request.data.copy()
        posts = Post.objects.exclude(deleted_at=None)
        result = PostSerializer(posts, many=True)
        return response_data(result.data)
    
    def restore_trash(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return response_data(message=validate.errors,status=STATUS['NO_DATA'])
        result = Post.objects.get(id=validate.data['id'])
        result.deleted_at = None
        result.save()
        serializer = PostSerializer(result)
        return response_data(message=SUCCESS['RESTORE_POST'], data=serializer.data)
    
    def delete_trash(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return response_data(message=validate.errors,status=STATUS['NO_DATA'])
        Post.objects.get(id=validate.data['id']).delete()
        return response_data(message=SUCCESS['DROP_POST'])
    
    def save_post(self, request):
        data = request.data.copy()
        post = SavePostValidate(data=data)
        if not post.is_valid():
            return response_data(message=post.errors,status=STATUS['NO_DATA'])
        try:
            exists_save_post = SavePost.objects.get(user_id=post.data['user_id'],post_id=post.data['post_id'])
            if exists_save_post.deleted_at is None:
                return response_data(message=ERROR['EXISTS_SAVE_POST'])
            exists_save_post.deleted_at = None
            exists_save_post.save()
            result = SavePostSerializer(exists_save_post)
            return response_data(message=SUCCESS['SAVE_POST'],data=result.data)
        except:
            result = SavePostSerializer(data=post.data)
            if not result.is_valid():
                return response_data(message=result.errors,status=STATUS['FAIL_REQUEST'])
            result.save()
            return response_data(message=SUCCESS['SAVE_POST'],data=result.data)
            
    def unsave_post(self, request, id):
        data = request.data.copy()
        validate = IdSavePostValidate(data={'id':id})
        if not validate.is_valid():
            return response_data(message=validate.errors,status=STATUS['NO_DATA'])
        save_post = SavePost.objects.get(id=validate.data['id'])
        save_post.deleted_at = datetime.now()
        save_post.save()
        result = SavePostSerializer(save_post)
        return response_data(message=SUCCESS['UNSAVE_POST'],data=result.data)
    
    def react_post(self, request):
        data = request.data.copy()
        post = PostReactValidate(data=data)
        if not post.is_valid():
            return response_data(message=post.errors,status=STATUS['NO_DATA'])
        try:
            exists_post_react = PostReact.objects.get(user_id=post.data['user_id'],post_id=post.data['post_id'])
            if exists_post_react.react is not 6:
                return response_data(message=ERROR['EXISTS_POST_REACT'], data={'id':exists_post_react.id})
            result = PostReactSerializer(exists_post_react, data=data)
            if not result.is_valid():
                return response_data(message=result.errors, status=STATUS['FAIL_REQUEST'])
            result.save()
            return response_data(message=SUCCESS['REACT_POST'],data=result.data)
        except:
            result = PostReactSerializer(data=post.data)
            if not result.is_valid():
                return response_data(message=result.errors,status=STATUS['FAIL_REQUEST'])
            result.save()
            return response_data(message=SUCCESS['REACT_POST'],data=result.data)
    
    def unreact_post(self, request, id):
        data = request.data.copy()
        validate = IdPostReactValidate(data={'id':id})
        if not validate.is_valid():
            return response_data(message=validate.errors,status=STATUS['NO_DATA'])
        save_post = PostReact.objects.get(id=validate.data['id'])
        save_post.react = 6
        save_post.save()
        result = PostReactSerializer(save_post)
        return response_data(message=SUCCESS['UN_REACT_POST'],data=result.data)