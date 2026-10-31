def product_0f_number(first_number,second_number):

    return first_number * second_number
    



square_list = list(map(square_number,[1, 2, 3, 4]))
print(square_list)
print(reduce(product_0f_number,square_list))
