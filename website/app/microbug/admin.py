from django.contrib import admin
from microbug.models import Version


class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['store_uuid', 'lines_of_code_count', 'previous_version']})
    ]

admin.site.register(Version, VersionAdmin)
