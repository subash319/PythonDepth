# 6. Write a program to count frequency of all words in a string.
# Split the string into words using whitespace as the separator.

str = input("Enter the string to count frequency of all words in a string:")
count = {}
words_seperated = str.lower().split()
for word in words_seperated:
    count[word] = count.get(word, 0) + 1
print(count)