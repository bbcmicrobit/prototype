import random
import microbug.settings as settings

# Read in the word list
WORD_LIST = [
    line.strip().lower()
    for line in open(settings.WORD_LIST_FILE,'r')
    if len(line)<6
]

def random_phrase(word_count):
    words = []
    for x in range(0, word_count):
        words.append(random_word())
    return '_'.join(words)

def random_word():
    return random.choice(WORD_LIST)
