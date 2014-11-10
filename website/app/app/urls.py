from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Route to the Django admin interface.
    url(r'^admin/', include(admin.site.urls)),

    # Route to the Microbug application.
    url(r'^microbug/', include("microbug.urls", namespace='microbug')),
)
