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

from django.contrib import admin
from microbug.models import Program, Tutorial, UserProfile, Version, FacilitatorRequest


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'realname', 'is_facilitator', 'email', 'has_pending_password_request')
    fieldsets = [
        (None, {'fields': ['user', 'facilitators', 'realname', 'email', 'has_pending_password_request']}),
        ('Questions', {'fields': [
            'question_1', 'question_2', 'question_3', 'question_4', 'question_5',
            'question_6', 'question_7', 'question_8', 'question_9', 'question_10'
        ]})
    ]

class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['store_uuid', 'lines_of_code_count', 'previous_version']})
    ]
    list_display = ('id', 'store_uuid', 'lines_of_code_count', 'is_compiled', 'python_pending_queue', 'python_compilation_eta', 'previous_version')

class FacilitatorRequestAdmin(admin.ModelAdmin):
    list_display = ('id','child','facilitator','is_pending','was_accepted','requested_at','resolved_at')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Program)
admin.site.register(Version, VersionAdmin)
admin.site.register(Tutorial)
admin.site.register(FacilitatorRequest, FacilitatorRequestAdmin)