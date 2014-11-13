from django.conf.urls import patterns, url
from microbug import views

urlpatterns = patterns('',
    # Normal urls

    # Ex: /
    url(r'^$', views.index, name='index'),

    # Ex: /programs
    url(r'^programs/$', views.programs, name='programs'),

    # Ex: /create_program
    url(r'^create_program/$', views.create_program, name='create_program'),

    # Ex: /program/23
    url(r'^program/(?P<program_id>\d+)', views.program, name='program'),

    # Ex: /program/23/big_new_programme
    url(r'^program/(?P<program_id>\d+)/(?P<program_name>.*)', views.program, name='program'),

    # Ex: /tutorials/juggling%20badgers
    url(r'^tutorial/(?P<tutorial_name>[^#]*)', views.tutorial, name='tutorial'),


    ###########################################################################

    # Ajax urls

    # Ex: /build_code :
    # { "program_name": program_name, "repr": { "code": python_code, "xml": xml_test } }
    #
    # Returns:
    # Program ID on success, BadRequest on failure.
    url(r'^build_code/$', views.build_code, name='build_code'),

    # Ex: /rename_program
    url(r'^rename_program/$', views.rename_program, name='rename_program'),
)