from django.urls import path,re_path

from dinner.views import join_dinner, management, Release, SingUp, sing_success, \
    MyEncoder, DisDinner, my_dinner

urlpatterns=[
    re_path(r'^join_dinner/$',join_dinner,name='join_dinner'),
    re_path(r'^management/$', management, name='management'),
    re_path(r'^release/$', Release.as_view(), name='release'),
    re_path(r'^sing_up/$', SingUp.as_view(), name='sing_up'),
    re_path(r'^sing_success/$', sing_success, name='sing_success'),
    # re_path(r'^dinner_list/$', dinner_list, name='dinner_list'),
    # re_path(r'^dinner_view/$', DinnerView, name='DinnerView'),
    re_path(r'^my_encoder/$', MyEncoder, name='MyEncoder'),
    re_path(r'^dis_dinner/$', DisDinner.as_view(), name='dis_dinner'),
    re_path(r'^my_dinner/$', my_dinner, name='dmy_dinner')

]
