# 4. Write a function that takes in a string and returns number of vowels and consonants in that string.

def count_vowel_consonants(str):
    vowel_count,consonant_count = 0,0
    vowels = ['a','e','i','o','u']
    for ch in str:
        if ch.isalpha():
            if ch.lower() in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count,consonant_count
print(count_vowel_consonants("Subash"))