from django.contrib import admin
from microbug.models import Version


class VersionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','store_uuid']})
    ]

admin.site.register(Version, VersionAdmin)
