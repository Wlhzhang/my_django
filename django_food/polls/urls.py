from django.urls import path, re_path, include
from rest_framework import routers

from polls import views
from polls.views import Login, Register, get_code, FindPassword, logout, dinner_home_fenye


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


#

urlpatterns=[
    re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^login/$',Login.as_view(),name='login'),
    re_path(r'^find_password/$', FindPassword.as_view(), name='find_password'),
    re_path(r'^register/$', Register.as_view(), name='register'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^home_fenye/$', dinner_home_fenye, name='homefenye'),
    path('', include(router.urls)),
]
