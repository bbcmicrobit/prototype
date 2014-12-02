from django.core.management.templates import TemplateCommand
import microbug.settings as settings
from django.contrib.auth.models import User, Group

class Command(TemplateCommand):

    help = "Sets up the system for basic use"

    def handle(self, user_count_str="1", **options):
        print("Setting up system ready for use")
        self._ensure_facilitators_exists()

    def _ensure_facilitators_exists(self):
        created, facilitators = Group.objects.get_or_create(name='facilitators')
        if created:
            print "Group 'Facilitators' has been created"
        else:
            print "Group 'Facilitators' already exists"
