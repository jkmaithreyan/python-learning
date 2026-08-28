words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def words_occurs_more_than_once(words):

    count = {}
    result = []

    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    for word in count:
        if count[word] > 1:
            result.append(word)

    return result

print(words_occurs_more_than_once(words))
