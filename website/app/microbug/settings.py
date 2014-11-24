# This file contains all of the Microbug specific settings

# How long to wait for a file lock before giving up
FILELOCK_TIMEOUT = 30

try:
    # Succeeds only on michael's machine :-)
    import michaels_machine
    BASE = "/home/michael/Work/CodeBug/MiniMicro/website/website/microbug_store"
except ImportError:
    # Are we running on the shared dev server?
    try:
        import sparkslabs
        BASE = "/srv/Websites/minimicro.iotoy.org/website/microbug_store"

    except ImportError:
        BASE = '/Users/molt/Documents/microbug_store'

# Where we're keeping the immutable store of xml/py data in JSON
PRIMARY_STORE_DIRECTORY = BASE + '/primary'

# The pending queue for the compiler
PENDING_PYTHON_QUEUE_DIRECTORY = BASE + '/pending'

# The directory where compiled programs will be stored by the compiler process
COMPILED_PYTHON_PROGRAMS_DIRECTORY = BASE + '/compiled'

# The time, in seconds, to process each Python item
PYTHON_ITEM_COMPILATION_TIME = 12