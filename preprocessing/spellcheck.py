'''
Spelling checker module with functions:

- correct_word
    - returns most likely spelling given word is misspelled, else returns original word
'''


import re
from os import path
from collections import Counter


WORD_DISTRIBUTION = Counter(re.findall(r'\w+', open(path.join(path.dirname(__file__), 'data/bnc_wiktionary_corpus.txt')).read().lower()))


#functions
def correct_word(word_string):
    '''
    Finds all valid one and two letter corrections for word_string, returning the word
    with the highest relative probability as type str.
    '''
    return max(find_candidates(word_string), key=find_word_prob)

def find_candidates(word_string):
    '''
    '''
    return (validate_words([word_string]) or validate_words(find_one_letter_edits(word_string)) or validate_words(find_two_letter_edits(word_string)) or [word_string])

def find_one_letter_edits(word_string):
    '''
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word_string[:i], word_string[i:]) for i in range(len(word_string) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def find_two_letter_edits(word_string):
    '''
    '''
    return (e2 for e1 in find_one_letter_edits(word_string) for e2 in find_one_letter_edits(e1))

def find_word_prob(word_string, N=sum(WORD_DISTRIBUTION.values())):
    '''
    '''
    return WORD_DISTRIBUTION[word_string] / N

def validate_words(word_list):
    '''
    '''
    #subset of words that appear in the dictionary created
    return set(word for word in word_list if word in WORD_DISTRIBUTION)
