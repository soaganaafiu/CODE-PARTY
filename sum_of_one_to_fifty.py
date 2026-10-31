from functools import reduce

def sum_numbers(num1, num2):

    return num1 + num2



number = range(1, 50)

print(reduce(sum_numbers, number))
