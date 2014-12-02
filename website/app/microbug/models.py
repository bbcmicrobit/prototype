from django.db import models
import settings
from compiled_version_store import CompiledVersionStore
from primary_version_store import PrimaryVersionStore
from pending_version_store import PendingVersionStore
import json
import datetime
import markdown
from django.contrib.auth.models import User
import collections
from random_phrase_generator import random_phrase

primary_version_store = PrimaryVersionStore(settings.PRIMARY_STORE_DIRECTORY)
pending_store = PendingVersionStore(settings.PENDING_PYTHON_QUEUE_DIRECTORY)
compiled_store = CompiledVersionStore(settings.COMPILED_PYTHON_PROGRAMS_DIRECTORY)


# This is an entire tutorial
class Tutorial(models.Model):
    # The name of the tutorial
    name = models.CharField(max_length=200)

    # The plaintext content of the program
    content = models.TextField(default="")

    # The content in HTML form
    def content_as_html(self):
        return markdown.markdown(self.content)

    # Stringifies as 'My Test Tutorial'
    def __str__(self):
        return self.name

# This stores additional details for a user beyond that which Django provides
class UserProfile(models.Model):
    # The User this profile is part of
    user = models.OneToOneField(User)

    # The facilitators of this user (Parents, teachers etc
    facilitators = models.ManyToManyField('UserProfile')

    # The programs that this user owns
    def programs_owned(self):
        return Program.objects.filter(owner=self)

    # The versions that this user owns
    def versions_owned(self):
        return Version.objects.filter(owner=self)

    # The programs contributed to but does not own
    def programs_contributed_to(self):
        sql_query = """
            SELECT * FROM microbug_program
            WHERE id IN (
              SELECT DISTINCT program_id
              FROM microbug_version
              WHERE owner_id=%s AND program_id NOT IN (
                SELECT id FROM microbug_program WHERE owner_id=%s
              )
            )
        """
        return Program.objects.raw(sql_query, [self.id, self.id])
    
    # Simple bit of stringification
    def __str__(self):
        return "{0}: {1}({2})".format(self.id, self.user.username, self.user.id)


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

    # This is the owner of the Version, may be blank for 'unowned' versions
    owner = models.ForeignKey(UserProfile, null=True, blank=True, default=None)

    # The program this is a version of, this makes things easy when new versions
    # of existing programs appear.
    # The 'related_name' stops Django creating a reverse Program.Version field, as
    # one exists.
    program = models.ForeignKey('Program', null=True, related_name='+')

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

    # Returns a boolean indicating if this version has been compiled
    def is_compiled(self):
        return compiled_store.contains(self.base_filename())
    is_compiled.boolean = True

    # The base filename
    def base_filename(self):
        return "{0}_{1}".format(self.id, self.store_uuid)
    base_filename.admin_order_field = 'id'
    base_filename.short_description = 'Base filename'

    # The position of this item in the pending queue (Actually the number of items to be
    # processed before this one).
    def python_pending_queue(self):
        return len(pending_store.items_before(self.base_filename()))

    # The ETA for the item being processed.
    def python_compilation_eta(self):
        # Add one, this item needs compiling itself
        time_in_seconds = settings.PYTHON_ITEM_COMPILATION_TIME * (self.python_pending_queue()+1)
        return datetime.timedelta(seconds=time_in_seconds)

    # Stringify as '1_bcff_2313 (11 LoC, base 2_dbff_2312')'
    def __str__(self):
        if self.previous_version is None:
            return "{0} ({1} LoC)".format(self.base_filename(), self.lines_of_code_count)
        else:
            return "{0} ({1} Loc, Prev: {2})".format(self.base_filename(), self.lines_of_code_count, self.previous_version.base_filename())

# The phrase used to edit the program
def default_edit_phrase():
    return random_phrase(settings.WORDS_IN_EDIT_PHRASES)

# This reflects a program
class Program(models.Model):
    # The name of the program, not guaranteed to be unique
    name = models.CharField(max_length=200)

    edit_phrase = models.CharField(
        max_length=200,
        default=default_edit_phrase
    )

    # edit_phrase = models.CharField(
    #     max_length=200,
    #     default=lambda: random_phrase(settings.WORDS_IN_EDIT_PHRASES)
    # )
    # A description of the program
    description = models.TextField(default="")

    # The time which the version was created by the user.
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    # The current version, all history between versions is stored within them.
    # The 'related_name' stops Django creating a version.program reverse as there's
    # already one there.
    version = models.ForeignKey(Version, related_name='+')

    # This is the owner of the Program, may be blank for 'unowned' programs
    owner = models.ForeignKey(UserProfile, null=True, blank=True, default=None)

    # Stringifies to '1: My Test Program' or '1: Unnamed Program'.
    def __str__(self):
        if self.name:
            return "{0}: {1}".format(self.id, self.name)
        else:
            return "{0}: Unnamed Program".format(self.id)

