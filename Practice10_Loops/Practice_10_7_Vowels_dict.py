# 7. Given a text string, create a dictionary in which keys are five vowels and
# values are the frequencies of those vowels in the string.

str = input("Please enter the string to calculate the number of vowels")
count_vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'u': 0}
for ch in str:
    if ch in count_vowels_dict:
        count_vowels_dict[ch] +=  1
print(count_vowels_dict)
