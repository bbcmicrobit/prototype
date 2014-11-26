from django.core.management.templates import TemplateCommand
import re
import random
import microbug.settings as settings
from django.contrib.auth.models import User

class Command(TemplateCommand):

    help = "Creates a number of users with randomised names and passwrods"
    word_list = [
        line.strip().lower()
        for line in open(settings.WORD_LIST_FILE,'r')
        if len(line)<6
    ]

    def handle(self, user_count_str="1", **options):
        MAXIMUM_USERS_TO_CREATE = 40
        if not re.match(r'^\d+$', user_count_str):
            print "Usage: python manage.py <number of users to create>"
            exit()

        user_count = int(user_count_str)
        if user_count == 1:
            print "Creating 1 user"
        if user_count > MAXIMUM_USERS_TO_CREATE:
            print "Cannot create more than {0} users".format(MAXIMUM_USERS_TO_CREATE)
            exit()
        else:
            print "Creating {0} users".format(user_count)

        for user_index in range(1, user_count+1):
            username = self.random_username()
            password = self.random_password()

            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()

            print "  {0}: {1} (PW: {2})".format(user_index, username, password)

    def random_username(self):
        while True:
            username = self.random_joined_string(settings.WORDS_IN_USERNAMES)
            user_count = User.objects.filter(username=username).count()
            if user_count==0:
                return username
            print("    Duplicate username '{0}".format(username))

    def random_password(self):
        return self.random_joined_string(settings.WORDS_IN_PASSWORDS)

    def random_joined_string(self, word_count):
        words = []
        for x in range(0, word_count):
            words.append(self.random_word())
        return '_'.join(words)

    def random_word(self):
        return random.choice(self.word_list)
