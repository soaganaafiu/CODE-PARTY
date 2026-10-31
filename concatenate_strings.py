from functools import reduce


def concatenate_words(first_word, second_word):
    return first_word + " " + second_word



word = ['I', 'love', 'Python']
print(reduce(concatenate_words, word))
