# 8. Write a function named find that takes in a list and a value.
# It should return True if that value is found in the list and False otherwise.
#
# Does your function work for strings, tuples, sets and dictionaries also ?

def find_value(L, v):
    return True if v in L else False

# It would work for all of them list,string,set and dictionary also
print(find_value({1:1,2:4,3:9,4:16}, 9))
