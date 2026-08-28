words = ["apple", "ant", "banana", "ball", "cat", "car"]

def longest_word_each_first_letter(words):

    result = {}

    for word in words:
        first_letter = word[0]
        if first_letter not in result:
            result[first_letter] = word
        else:
            if len(word) > len(result[first_letter]):
                result[first_letter] = word

    return result

print(longest_word_each_first_letter(words))


       
