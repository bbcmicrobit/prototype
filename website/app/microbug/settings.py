import os

# This file contains all of the Microbug specific settings

# How long to wait for a file lock before giving up
FILELOCK_TIMEOUT = 30

try:
    # Succeeds only on michael's machine :-)
    import michaels_machine
    STORE_BASE = "/home/michael/Work/CodeBug/MiniMicro/website/website/microbug_store"
    DJANGO_BASE = "/home/michael/Work/CodeBug/MiniMicro/website/website/app"
except ImportError:
    # Are we running on the shared dev server?
    try:
        import sparkslabs
        STORE_BASE = "/srv/Websites/minimicro.iotoy.org/website/microbug_store"
        DJANGO_BASE = '/srv/Websites/minimicro.iotoy.org/website/app'

    except ImportError:
        # Are we running on the taster machine?
        try:
            import taster_machine
            STORE_BASE = "/srv/projects/microbug/website/microbug_store"
            DJANGO_BASE = "/srv/projects/microbug/website/app"

        except ImportError:
            if os.path.exists('/Users/molt/Documents/microbug_store'):
                STORE_BASE = '/Users/molt/Documents/microbug_store'
                DJANGO_BASE = '/Users/molt/Documents/microbug/website/app'
            elif os.path.exists('/Users/mattbr/Store/microbug'):
                STORE_BASE = '/Users/mattbr/Store/microbug'
                DJANGO_BASE = '/Users/mattbr/Sites/microbug/website/app'
            else:
                raise Exception("Cannot find possible store")

# Check the directories exist
if not os.path.exists(STORE_BASE):
    raise Exception("Cannot find store at '{0}', check settings.py".format(STORE_BASE))
if not os.path.exists(DJANGO_BASE):
    raise Exception("Cannot find Django app at '{0}, check settings.py".format(DJANGO_BASE))

# Where we're keeping the immutable store of xml/py data in JSON
PRIMARY_STORE_DIRECTORY = STORE_BASE + '/primary'

# The pending queue for the compiler
PENDING_PYTHON_QUEUE_DIRECTORY = STORE_BASE + '/pending'

# The directory where compiled programs will be stored by the compiler process
COMPILED_PYTHON_PROGRAMS_DIRECTORY = STORE_BASE + '/compiled'

# The directory where failed compiles programs will be stored by the compiler process
FAIL_COMPILED_PYTHON_PROGRAMS_DIRECTORY = STORE_BASE + '/failed_compiles'

# The directory that the Tutorial Assets live in for the static server
TUTORIAL_ASSETS_STATIC_DIRECTORY = DJANGO_BASE + '/microbug/static/bug/tutorial_assets'

# The word list to use for usernames/passwords
WORD_LIST_FILE = '/usr/share/dict/words'
try:
   import taster_machine
   WORD_LIST_FILE = "/home/codebug/microbug/website/app/app/wordlist"
except ImportError:
   pass

# The time, in seconds, to process each Python item
PYTHON_ITEM_COMPILATION_TIME = 12

# Controls the complexity of usernames, passwords, and edit phrases.
WORDS_IN_USERNAMES = 2
WORDS_IN_PASSWORDS = 2
WORDS_IN_EDIT_PHRASES = 1
