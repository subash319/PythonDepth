# 1. Input two strings s1 and s2 and then create a list that contains all the common characters of the two input
# strings.

s1 = input("Enter the first string:")
s2 = input("Enter the second string:")
set_string1 = set(s1)
set_string2 = set(s2)
print(set_string1)
print(set_string2)
print(set_string1 & set_string2)
print(set_string1.intersection(set_string2))