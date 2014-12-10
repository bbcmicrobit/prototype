import random
import microbug.settings as settings
from django.contrib.auth.models import User

# Read in the word list
WORD_LIST = [
    line.strip().lower()
    for line in open(settings.WORD_LIST_FILE,'r')
    if len(line)<6
]

# Return a single random word from the list
def random_word():
    return random.choice(WORD_LIST)

# Return a number of random words from the list, all joined with _s.
def random_phrase(word_count):
    words = []
    for x in range(0, word_count):
        words.append(random_word())
    return '_'.join(words)

# Returns a random unused username
def random_username():
    while True:
        username = random_phrase(settings.WORDS_IN_USERNAMES)
        user_count = User.objects.filter(username=username).count()
        if user_count==0:
            return username

# Returns a random unused password
def random_password():
    return random_phrase(settings.WORDS_IN_PASSWORDS)
