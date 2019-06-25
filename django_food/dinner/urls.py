from django.urls import path,re_path

from dinner.views import join_dinner, management, release, sing_up, sing_success

urlpatterns=[

    re_path(r'^join_dinner/$',join_dinner,name='join_dinner'),
    re_path(r'^management/$', management, name='management'),
    re_path(r'^release/$', release, name='release'),
    re_path(r'^sing_up/$', sing_up, name='sing_up'),
    re_path(r'^sing_success/$', sing_success, name='sing_success'),
]
