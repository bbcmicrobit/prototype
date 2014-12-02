from django.contrib import admin
from microbug.models import Program, Tutorial, UserProfile, Version


class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['store_uuid', 'lines_of_code_count', 'previous_version']})
    ]
    list_display = ('id', 'store_uuid', 'lines_of_code_count', 'is_compiled', 'python_pending_queue', 'python_compilation_eta', 'previous_version')


admin.site.register(UserProfile)
admin.site.register(Program)
admin.site.register(Version, VersionAdmin)
admin.site.register(Tutorial)

