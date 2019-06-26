from django.urls import path,re_path

from polls.views import Login, forget_password, Register, get_code, FindPassword,logout

urlpatterns=[
    # # re_path('get_register/$',get_register,name='get_register'),
    # re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^get_code/$', get_code, name='getcode'),

    re_path(r'^login/$',Login.as_view(),name='login'),
    re_path(r'^forget_password/$', forget_password, name='forget_password'),
    re_path(r'^find_password/$', FindPassword.as_view(), name='find_password'),
    re_path(r'^register/$', Register.as_view(), name='register'),
    re_path(r'^logout/$', logout, name='logout'),

    # re_path(r'^register/$', Register.as_view(), name='register')
]
