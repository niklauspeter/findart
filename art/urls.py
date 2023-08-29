from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'art-home'),
    path('about/',views.about,name = 'art-about'),
]
