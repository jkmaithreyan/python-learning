def second_most_frequent_char(word):

    count_char = {}

    for char in word:
        if char not in count_char:
            count_char[char] = 1
        else:
            count_char[char] += 1

    highest_count = 0
    second_highest_count = 0

    most_frequent = None
    second_most_frequent = None

    for char in count_char:

        if count_char[char] > highest_count:

            second_highest_count = highest_count
            second_most_frequent = most_frequent

            highest_count = count_char[char]
            most_frequent = char

        elif count_char[char] < highest_count and count_char[char] > second_highest_count:

            second_highest_count = count_char[char]
            second_most_frequent = char

    return second_most_frequent


word = "aabbbccccdd"
print(second_most_frequent_char(word))