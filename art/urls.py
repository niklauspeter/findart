from django.urls import path
from . import views
from .views import (PostListView, 
PostDetailView, 
PostCreateView,
PostUpdateView,
PostDeleteView,
AddCommentView
)

urlpatterns=[
    path('',views.home,name = 'art-home'),
    path('home/',PostListView.as_view(),name = 'post-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post-delete'),
    path('about/',views.about,name = 'art-about'),
    path('landing/',views.landing,name = 'art-landing'),
    path('get_messages/<int:conversation_id>/', views.get_messages, name='get_messages'),
    path('send_message/<int:conversation_id>/', views.send_message, name='send_message'),
    path('post<int:pk>/comment/',AddCommentView.as_view(),name = 'add_comment'),
]
