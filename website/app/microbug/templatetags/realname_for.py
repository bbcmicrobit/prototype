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

import datetime
from django import template
from microbug.models import UserProfile

register = template.Library()

@register.simple_tag
def realname_for(user_id):
    user_profile = UserProfile.objects.get(pk=user_id)

    if user_profile and user_profile.realname is not None and user_profile.realname != "":
        return user_profile.realname
    else:
        # Lorem ipsum
        return 'No name set'
