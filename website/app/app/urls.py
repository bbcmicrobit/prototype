from django.conf.urls import patterns, include, url
from django.contrib import admin

try:
    import michaels_machine

    urlpatterns = patterns('',
        # Route to the Django admin interface.
        url(r'^admin/', include(admin.site.urls)),

        # Route to the Microbug application.
        url(r'^', include("microbug.urls", namespace='microbug')),
    )

except ImportError:

    urlpatterns = patterns('',
        # Route to the Django admin interface.
        url(r'^admin/', include(admin.site.urls)),

        # Route to the Microbug application.
        url(r'^microbug/', include("microbug.urls", namespace='microbug')),
    )
