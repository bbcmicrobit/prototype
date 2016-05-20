#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import random
import microbug.settings as settings
from django.contrib.auth.models import User

# Read in the word list
WORD_LIST = [
    line.strip().lower()
    for line in open(settings.WORD_LIST_FILE,'r')
    if len(line)<11
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
        if len(username) < 16:
            user_count = User.objects.filter(username=username).count()
            if user_count==0:
                return username

# Returns a random unused password
def random_password():
    return random_phrase(settings.WORDS_IN_PASSWORDS)

# Returns a random edit phrase
def random_edit_phrase():
    return random_phrase(settings.WORDS_IN_EDIT_PHRASES)
