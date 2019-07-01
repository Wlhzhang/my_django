from django.urls import path,re_path

from person.views import applyhost, detail, GetMen, ModifyPassword, get_jilian

urlpatterns=[
    re_path(r'^get_men/$',GetMen.as_view(),name='get_men'),
    re_path(r'^applyhost/$', applyhost, name='applyhost'),
    re_path(r'^detail/$', detail, name='detail'),
    re_path(r'^modify_password/$', ModifyPassword.as_view(), name='modify_password'),
    re_path(r'get_jilian/$', get_jilian, name='get_jilian')

]

