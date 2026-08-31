def is_anagram(word1, word2):

    word1_count = {}
    word2_count = {}

    for char in word1:
        if char not in word1_count:
            word1_count[char] = 1
        else:
            word1_count[char] += 1

    for char in word2:
        if char not in word2_count:
            word2_count[char] = 1
        else:
            word2_count[char] += 1

    return word1_count == word2_count

word1 = str(input("enter word 1: "))
word2 = str(input("enter word 2: "))

print(is_anagram(word1, word2))