#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from django.conf.urls import patterns, include, url
from django.contrib import admin

#default
urlpatterns = patterns('',
    # Route to the Django admin interface.
    url(r'^admin/', include(admin.site.urls)),

    # Route to the Microbug application.
    url(r'^bug/', include("microbug.urls", namespace='microbug')),
)


try:
    # Are we running on michael's dev machine?
    import michaels_machine

    urlpatterns = patterns('',
        # Route to the Django admin interface.
        url(r'^admin/', include(admin.site.urls)),

        # Route to the Microbug application.
        url(r'^', include("microbug.urls", namespace='microbug')),
    )

except ImportError:
    pass

try:
    # Are we running on the dev server?
    import sparkslabs

    urlpatterns = patterns('',
        # Route to the Django admin interface.
        url(r'^admin/', include(admin.site.urls)),

        # Route to the Microbug application.
        url(r'^', include("microbug.urls", namespace='microbug')),
    )

except ImportError:
    pass


try:
    # Are we running on the taster server?
    import taster_machine

    urlpatterns = patterns('',
        # Route to the Django admin interface.
        url(r'^admin/', include(admin.site.urls)),

        # Route to the Microbug application.
        url(r'^', include("microbug.urls", namespace='microbug')),
    )

except ImportError:
    pass




