from django.contrib import admin
from microbug.models import Program, Version


class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['store_uuid', 'lines_of_code_count', 'previous_version']})
    ]


admin.site.register(Program)
admin.site.register(Version, VersionAdmin)

