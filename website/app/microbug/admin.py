from django.contrib import admin
from microbug.models import Program, Tutorial, UserProfile, Version, FacilitatorRequest


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_facilitator', 'has_pending_password_request')
    fieldsets = [
        (None, {'fields': ['user', 'facilitators', 'realname', 'has_pending_password_request']}),
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