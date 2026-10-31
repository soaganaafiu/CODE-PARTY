def palindrome(word):

    reversed_word = word[::-1]

    return word == reversed_word



words = ['level', 'world', 'madam', 'python']

print(list(filter(palindrome, words)))
