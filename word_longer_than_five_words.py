def longer_than_five_words(word):

    return len(word) > 5





words = ['cat', 'elephant', 'tiger', 'lion']
print(list(filter(longer_than_five_words, words)))
