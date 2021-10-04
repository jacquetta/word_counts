"""Count words in file."""
import sys

# put your code here.
def count_words(file):

    lines = open(file)

    dic_words = {}
    list_words = []
    for line in lines:
        line = line.rstrip()
        list_words = line.split(" ")
        for word in list_words:
            dic_words[word] = dic_words.get(word, 0) + 1
    lines.close()
    for key, value in dic_words.items():
        print(f"{key} {value}")
    return dic_words

count_words("test.txt")

def tokenize(filename):
    lines = open(filename)
    list_words = []
    for line in lines:
        line = line.rstrip()
        list_words = line.split(" ")
    lines.close()
    return list_words

def count_words(words):
    dic_words = {}
    for word in words:
        dic_words[word] = dic_words.get(word, 0) + 1
    return dic_words

def print_word_counts(word_counts):
    for key, value in word_counts.items():
        print(f"{key} {value}")
    return word_counts

