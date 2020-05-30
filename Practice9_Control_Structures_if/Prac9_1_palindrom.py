# 1. Write a program that enters a string and prints whether it is a palindrome. Ignore case and spaces,
# so that all expressions like 'Nurses run'   'Madam I am Adam' are considered palindromes.

# My Answer
str_pal = input("Please enter the string to check palindrome:")
list_str_pal = list(str_pal.lower().replace(' ', ''))
print(list_str_pal)
print(list_str_pal[::-1])
print('The string is palindrome' if list_str_pal == list_str_pal[::-1] else 'The string is not palindrome')

# Deepali's lecturer Answer
s = input('Enter a string : ')
if s.replace(' ', '').lower() == s[::-1].replace(' ', '').lower():
   print('String is a palindrome')
else:
   print('String is not a palindrome')
