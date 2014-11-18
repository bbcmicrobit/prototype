# This file contains all of the Microbug specific settings

# How long to wait for a file lock before giving up
FILELOCK_TIMEOUT = 30

# Where we're keeping the immutable store of xml/py data in JSON
PRIMARY_STORE_DIRECTORY = '/Users/molt/Documents/microbug_store/primary'

# The pending queue for the compiler
PENDING_PYTHON_QUEUE_DIRECTORY = '/Users/molt/Documents/microbug_store/pending'

# The directory where compiled programs will be stored by the compiler process
COMPILED_PYTHON_PROGRAMS_DIRECTORY = '/Users/molt/Documents/microbug_store/compiled'

# The time, in seconds, to process each Python item
PYTHON_ITEM_COMPILATION_TIME = 12