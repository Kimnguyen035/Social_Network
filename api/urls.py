from django.contrib import admin
from django.urls import path
# from .views.auth_view import AuthView
from .views.post_view import PostView

url_post = [
    path('all-post', PostView.as_view({'get':'all_post'})),
    path('detail-post', PostView.as_view({'get':'detail_post'})),
    path('get-trash', PostView.as_view({'get':'get_trash'})),
    
    path('post-blog', PostView.as_view({'post':'post_blog'})),
    path('save-post', PostView.as_view({'post':'save_post'})),
    path('react-post', PostView.as_view({'post':'react_post'})),
    
    path('edit-post/<int:id>', PostView.as_view({'put':'edit_post'})),
    path('unreact-post/<int:id>', PostView.as_view({'put':'unreact_post'})),
    
    path('delete-post/<int:id>', PostView.as_view({'delete':'delete_post'})),
    path('restore-post/<int:id>', PostView.as_view({'delete':'restore_trash'})),
    path('drop-post/<int:id>', PostView.as_view({'delete':'delete_trash'})),
    path('unsave-post/<int:id>', PostView.as_view({'delete':'unsave_post'})),
]

urlpatterns = []

urlpatterns += url_post