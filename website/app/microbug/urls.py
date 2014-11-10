from django.conf.urls import patterns, url
from microbug import views

urlpatterns = patterns('',
    # Ex: /microbug
    url(r'^$', views.index, name='index'),
    url(r'^build_code/$', views.build_code, name='build_code'),
)