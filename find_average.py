def find_average_of_a_list(numbers):

    sum = 0
    average = 0

    for num in numbers:
        sum += num

    average = sum / len(numbers)

    return average

numbers = [10, 20, 30, 40, 50]
print(find_average_of_a_list(numbers))