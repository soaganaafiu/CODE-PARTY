def numbers_divisible_by_three_and_five(number):

    return number % 3 == 0 and number % 5 == 0




numbers = range(1, 51)
print(list(filter(numbers_divisible_by_three_and_five, numbers)))
