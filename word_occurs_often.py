words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def words_occurs_often(words):

    count = {}
    result = ""
    highest_count = 0
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    for values in count:
        if count[values] > highest_count:
            highest_count = count[values]
            result = values

    return result

print(words_occurs_often(words))
            

