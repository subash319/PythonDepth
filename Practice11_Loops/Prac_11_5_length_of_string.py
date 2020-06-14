# 5. Write a program that finds the shortest and the longest string from a list of strings.

list_of_strings = ['subash', 'chandra', 'Elluri', 'harini', 'darapu', 'abc', 'xy', 'I dont care']

longest_length = shortest_length = len(list_of_strings[0])
for string in list_of_strings:
    if len(string) >= longest_length:
        longest_string = string
        longest_length = len(string)
    if len(string) <= shortest_length:
        shortest_string = string
        shortest_length = len(string)

print(f'The longest string is {longest_string} with length {longest_length}')
print(f'The shortest string is {shortest_string} with length {shortest_length}')