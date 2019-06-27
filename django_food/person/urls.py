from django.urls import path,re_path

from person.views import applyhost, detail, message, my_messages, \
    verified_bind_done, GetMen

urlpatterns=[
    # # re_path('get_register/$',get_register,name='get_register'),
    # re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^get_men/$',GetMen.as_view(),name='get_men'),
    re_path(r'^applyhost/$', applyhost, name='applyhost'),
    re_path(r'^detail/$', detail, name='detail'),
    re_path(r'^message/$', message, name='message'),
    re_path(r'^my_messages/$', my_messages, name='my_messages'),
    re_path(r'^verified_bind_done/$', verified_bind_done, name='verified_bind_done'),

]
