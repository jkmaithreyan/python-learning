def groupby_first_letter(words):

    result = {}

    for word in words:
        first_letter = word[0]

        if first_letter not in result:
            result[first_letter] = [word]
        else:
            result[first_letter].append(word)

    return result 


words = ["apple", "ant", "banana", "ball", "cat"]
print(groupby_first_letter(words))