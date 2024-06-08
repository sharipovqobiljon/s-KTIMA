from django.urls import path
from .views import Home,SignUp,news,connect
urlpatterns=[
    path('',Home.as_view(),name="home"),
    path('signup',SignUp.as_view(),name='signup'),
    path('news',news.as_view(),name="news"),
    path('connect',connect.as_view(),name='connect')
]