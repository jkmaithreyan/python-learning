def number_grater_than_average(numbers):

    total = 0
    result = []

    for num in numbers:
        total += num

    average = total / len(numbers)

    for num in numbers:
        if num > average:
            result.append(num)

    return result

numbers = [10, 20, 30, 40, 50]
print(number_grater_than_average(numbers))