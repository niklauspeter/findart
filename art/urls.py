from django.urls import path
from . import views
from .views import (PostListView, 
PostDetailView, 
PostCreateView,
PostUpdateView,
PostDeleteView
)

urlpatterns=[
    # path('',views.home,name = 'art-home'),
    path('',PostListView.as_view(),name = 'art-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post-delete'),
    path('about/',views.about,name = 'art-about'),
    path('landing/',views.landing,name = 'art-landing'),
]
