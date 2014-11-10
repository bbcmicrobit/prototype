from django.conf.urls import patterns, url
from microbug import views

urlpatterns = patterns('',
    # Ex: /microbug
    url(r'^$', views.index, name='index'),
)