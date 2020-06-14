#  11. What is wrong in the following code.
#
# text = input('Enter some text : ')
# ch = input('Enter a character : ')
# i = 0
# while  text[i]!=ch and i<len(text) :
#    i+=1
# print(f'{ch} appears at index {i} in {data}')
# The following two exercises(12 and 13) ask you to print pyramid patterns.
#  They might not be of practical use but are helpful in understanding loops and are very interesting.

text = input('Enter some text : ')
ch = input('Enter a character : ')
i = 0
while  text[i] != ch and i < len(text) :
   i+=1
print(f'{ch} appears at index {i} in {text}')