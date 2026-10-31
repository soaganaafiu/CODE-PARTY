def greater_than_two(value):

    return value[0] > 2


values = [(1, "A"), (4, "B"), (2, "C")]

print(list(filter(greater_than_two, values)))
