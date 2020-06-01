# 3. Write a program that counts the number of vowels, consonants and digits in a string.

str_to_be_counted = input("Enter the string to count the vowels and consonants")

vowels = list('aeiou')
consonants = list('bcdfghjklmnopqrstvwxyz')
count_vowels = 0
count_conson = 0
count_digit = 0
for ch in str_to_be_counted:
    if ch.lower() in vowels:
        count_vowels += 1
    elif ch.lower() in consonants:
        count_conson += 1
    elif ch.isdigit():
        count_digit += 1
print(f'count_vowels:{count_vowels}')
print(f'count_consonants:{count_conson}')
print(f'count_digits:{count_digit}')
