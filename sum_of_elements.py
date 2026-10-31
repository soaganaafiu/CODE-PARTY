def sum_of_elements(numbers):

    answer = []

    for number in numbers:

        total = 0 

        for index in number:

            total += index

        answer.append(total)  

    return answer


values = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]  

print(sum_of_elements(values))
