from django.db import models
import settings
from primary_version_store import PrimaryVersionStore
import json

primary_version_store = PrimaryVersionStore(settings.PRIMARY_STORE_DIRECTORY)

# This reflects a single version which the user has uploaded
class Version(models.Model):
    # The UUID in the file store
    store_uuid = models.CharField(max_length=64)

    # The number of lines of code in the Python file
    lines_of_code_count = models.IntegerField()

    # The time which the version was created by the user.
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    # The previous version for this.  Optional
    previous_version = models.ForeignKey('self', blank=True, null=True)

    # Returns the JSON from the primary store
    def json(self):
        json_str = primary_version_store.retrieve(self.base_filename())
        return json.loads(json_str)

    # Reads the JSON from the primary store and returns the Python code stored therein
    def code(self):
        return self.json()['repr']['code']

    # Reads the JSON from the primary store and returns the Blockly XML stored therein
    def xml(self):
        return self.json()['repr']['xml']

    # The base filename
    def base_filename(self):
        return "{0}_{1}".format(self.id, self.store_uuid)
    base_filename.admin_order_field = 'id'
    base_filename.short_description = 'Base filename'

    # Stringify as '1_bcff_2313 (11 LoC, base 2_dbff_2312')'
    def __str__(self):
        if self.previous_version is None:
            return "{0} ({1} LoC)".format(self.base_filename(), self.lines_of_code_count)
        else:
            return "{0} ({1} Loc, Prev: {2})".format(self.base_filename(), self.lines_of_code_count, self.previous_version.base_filename())


# This reflects a program
class Program(models.Model):
    # The name of the program, not guaranteed to be unique
    name = models.CharField(max_length=200)

    # A description of the program
    description = models.TextField(default="")

    # The time which the version was created by the user.
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    # The current version, all history between versions is stored within them
    version = models.ForeignKey(Version)

    # Stringifies to '1: My Test Program' or '1: Unnamed Program'.
    def __str__(self):
        if self.name:
            return "{0}: {1}".format(self.id, self.name)
        else:
            return "{0}: Unnamed Program".format(self.id)