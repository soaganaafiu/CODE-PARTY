#def even_number(number):
#
#    for index in range(1, 21):
#
#        return index % 2 == 0
#
#
#print(list(filter(even_number)))




def even_number(number):

    return number % 2 == 0


print(list(filter(even_number, range(1, 21))))
