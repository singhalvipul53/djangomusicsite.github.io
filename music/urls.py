from django.urls import path
from . import views

urlpatterns=[
    path('home1/',views.home1,name='home1'),
    path('',views.home,name='home'),
    path('userpage/',views.userpage,name='userpage'),
    path('userhome/',views.userhome,name='userhome'),
    path('artistdetail/<str:pk>',views.artistdetail,name='artistdetail'),
    path('songdetail/<str:pk>',views.songdetail,name='songdetail'),
    path('account_setting/',views.account_setting,name='account_setting'),
    path('playlist/<str:pk>',views.playlist,name='playlist'),
    path('createplaylist/<str:pk>',views.createplaylist,name='createplaylist'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
