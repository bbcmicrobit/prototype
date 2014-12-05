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

    # Ex: /download/23/big_new_programme
    url(r'^download/(?P<program_id>\d+)/(?P<program_name>.*)', views.download, name='download'),

    # Ex: /download/23
    url(r'^download/(?P<program_id>\d+)', views.download, name='download'),

    # Ex: /program/23
    url(r'^program/(?P<program_id>\d+)', views.program, name='program'),

    # Ex: /program/23/big_new_programme
    url(r'^program/(?P<program_id>\d+)/(?P<program_name>.*)', views.program, name='program'),

    # Ex: /register_user
    url(r'^register_user', views.register_user, name='register_user'),

    # Ex: /tutorials/juggling%20badgers
    url(r'^tutorial/(?P<tutorial_name>[^#]*)', views.tutorial, name='tutorial'),

    # Ex: /user/23
    url(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),

    ###########################################################################

    # Ajax urls

    # Ex: /authenticate_user
    # { "username": username, "password": password }
    url(r'^authenticate_user/$', views.authenticate_user, name='authenticate_user'),

    # Ex: /build_code :
    # { "program_name": program_name, "repr": { "code": python_code, "xml": xml_test } }
    #
    # Returns:
    # Program ID on success, BadRequest on failure.
    url(r'^build_code/$', views.build_code, name='build_code'),

    # Ex: /facilitor_request
    # { 'facilitator-name: name }
    url(r'^facilitator_request', views.facilitator_request, name='facilitator_request'),

    # Ex: /login_pane
    # Returns either the login pane, or the 'signed in' pane.  Allows Django templates to be
    # used for this partial.
    url(r'^login_pane', views.login_pane, name='login_pane'),

    # Ex: /queue_status/23
    url(r'^queue_status/(?P<program_id>\d+)', views.queue_status, name='queue_status'),

    # Ex: /rename_program
    url(r'^rename_program/$', views.rename_program, name='rename_program'),

    # Ex: /respond_to_facilitator_request
    # {'request_id': request_id, 'is_accepted': true/false}
    url(r'^respond_to_facilitator_request', views.respond_to_facilitator_request, name='respond_to_facilitator_request'),

    # Ex: /sign_out
    url(r'^sign_out/$', views.sign_out, name='sign_out'),

    # Ex: /update_user_details
    # {'name': real_name, 'question_answers': [ans1, ans2, ans 3 ... ans10]}
    url(r'^update_user_details/$', views.update_user_details, name='update_user_details')
)