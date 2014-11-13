from django.conf.urls import patterns, url
from microbug import views

urlpatterns = patterns('',
    # Ex: /
    url(r'^$', views.index, name='index'),

    # Ex: /programs
    url(r'^programs/$', views.programs, name='programs'),

    # Ex: /create_program
    url(r'^create_program/$', views.create_program, name='create_program'),

    # Ex: /build_code (Called via the button, will be Ajaxified)
    url(r'^build_code/$', views.build_code, name='build_code'),

    # Ex: /program/23
    url(r'^program/(?P<program_id>\d+)', views.program, name='program'),

    # Ex: /program/23/big_new_programme
    url(r'^program/(?P<program_id>\d+)/(?P<program_name>.*)', views.program, name='program'),
)