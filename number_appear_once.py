def num_appear_only_once(numbers):

    for num in numbers:
        if numbers.count(num) == 1:
            return num


numbers = [4, 1, 2, 1, 2]
print(num_appear_only_once(numbers))