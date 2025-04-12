from django.urls import path
from .views import create_post, get_posts, delete_post, PostList, update_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('posts/', get_posts, name='get_posts'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('list/', PostList.as_view(), name='post_list'),
    path('update/<int:pk>/', update_post, name='update_post'),
]
