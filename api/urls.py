from django.contrib import admin
from django.urls import path
from .views.auth_view import AuthView
from .views.post_view import PostView
from .views.group_view import GroupView

url_post = [
    path('all-post', PostView.as_view({'get':'all_post'})),
    path('detail-post/<int:id>', PostView.as_view({'get':'detail_post'})),
    path('get-trash', PostView.as_view({'get':'get_trash'})),
    path('all-save-post', PostView.as_view({'get':'get_all_save_post'})),
    
    path('post-blog', PostView.as_view({'post':'post_blog'})),
    path('save-post', PostView.as_view({'post':'save_post'})),
    path('react-post', PostView.as_view({'post':'react_post'})),
    path('comment-post', PostView.as_view({'post':'comment_post'})),
    
    path('edit-post/<int:id>', PostView.as_view({'put':'edit_post'})),
    path('unreact-post/<int:id>', PostView.as_view({'put':'unreact_post'})),
    
    path('delete-post/<int:id>', PostView.as_view({'delete':'delete_post'})),
    path('restore-post/<int:id>', PostView.as_view({'delete':'restore_trash'})),
    path('drop-post/<int:id>', PostView.as_view({'delete':'delete_trash'})),
    path('unsave-post/<int:id>', PostView.as_view({'delete':'unsave_post'})),
    path('delete-comment/<int:id>', PostView.as_view({'delete':'delete_comment'})),
]

url_group = [
    path('all-group', GroupView.as_view({'get':'get_all_group'})),
    path('detail-group/<int:id>', GroupView.as_view({'get':'detail_group'})),
    
    path('add-group', GroupView.as_view({'post':'add_group'})),
    
    path('delete-group/<int:id>', GroupView.as_view({'delete':'delete_group'})),
]

urlpatterns = []

urlpatterns += url_post + url_group