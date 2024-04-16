"""
Count the occurrences of all words in a text
and write them to a CSV-file.
"""

import string
from collections import Counter

import utilities as util


def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    stripped = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in stripped if word]
    word_counts = Counter(word_list)
    return word_counts


with open('frankenstein.txt', 'r') as reader:
    word_counts = count_words(reader)
util.collection_to_csv(word_counts, num=100)
