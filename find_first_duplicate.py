def find_first_duplicate_number(numbers):

    duplicate_number = 0
    copy_numbers = []

    for num in numbers:
        if num not in copy_numbers:
            copy_numbers.append(num)
        else:
            duplicate_number = num
            break

    return duplicate_number

numbers = [1, 2, 3, 4, 2, 5, 3]
print(find_first_duplicate_number(numbers))