# 5. Write a program to count frequency of all characters in a string.

# str = input("Enter the string to count the frequency of all characters")
# list_count = [0] * 26
# for ch in str:
#     i = ord(ch.lower())
#     list_count[i-97] += 1
# print(f'After:{list_count}')
# i = 0
# for count_each in list_count:
#     if count_each >= 1:
#         print(f"The frequency of the alphabet {chr(i+97)} is {count_each} ")
#     i += 1

str = input("Enter the string to count the frequency of all characters")
count = {}
for character in str:
    count[character] = count.get(character, 0)+1
print(count)