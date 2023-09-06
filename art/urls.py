from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns=[
    # path('',views.home,name = 'art-home'),
    path('',PostListView.as_view(),name = 'art-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('about/',views.about,name = 'art-about'),
    path('landing/',views.landing,name = 'art-landing'),
]
