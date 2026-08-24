def word_with_most_vowels(words):
    
    vowels = "aeiou"
    higher_vowel_count = 0
    result = None

    for word in words:
        vowel_count = 0

        for char in word:
            if char in vowels:
                vowel_count += 1

        if vowel_count > higher_vowel_count:
            higher_vowel_count = vowel_count
            result = word

    return result

words = ["apple", "banana", "education", "sky"]
print(word_with_most_vowels(words))