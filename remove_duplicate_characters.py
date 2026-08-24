def Remove_duplicate_characters(word):

    result = ""

    for char in word:
        if char not in result:
            result += char

    return result

print(Remove_duplicate_characters("programming"))