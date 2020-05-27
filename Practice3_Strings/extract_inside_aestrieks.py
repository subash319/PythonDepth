# 4. Write a program to extract whatever is enclosed inside asterisks in a string.
# For example if the string is 'Raj 35 *14/12/1978* Paris', the portion extracted is 14/12/1978
#
# (Hint : Use index() and rindex() methods)

s = 'Raj 35 *14/12/1978* Paris'
# Returns the index of first occurence of the substring
left_index = s.index('*')
# Returns the index of the last occurence of the substring
right_index = s.rindex('*')
print(f'left index : {left_index}, right index: {right_index}')
print(s[(left_index + 1):right_index])
