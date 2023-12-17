# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/', views.user_login, name='user_login'),
    path('signup/', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/share/', views.share_post, name='share_post'),  
    path('post/<int:pk>/rate/', views.rate_post, name='rate_post'),


    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
]

