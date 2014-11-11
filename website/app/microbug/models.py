from django.db import models
from django.utils import timezone
import datetime


# This reflects a single version which the user has uploaded
class Version(models.Model):
    # The name of the version, not guaranteed to be unique
    name = models.CharField(max_length=200)

    # The time which the version was created by the user.
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    # The UUID in the file store
    store_uuid = models.CharField(max_length=64)

    # The base filename
    def base_filename(self):
        return "{0}_{1}".format(self.id, self.store_uuid)

    base_filename.admin_order_field = 'id'
    base_filename.short_description = 'Base filename'

    # Stringify as 'My Demo Program (1_bcff_2313)'
    def __str__(self):
        return "{0} ({1})".format(self.name, self.base_filename())
