# 1. Write a function that multiplies all the entries of a list by a number.

number = 2
def multilply_by_number(list_to_be_multiplied):
    for i, num in enumerate(list_to_be_multiplied):
        list_to_be_multiplied[i]= num*number
        print(i)
    print(list_to_be_multiplied)
list_mul = [1,2,3,4,5,6]
multilply_by_number(list_mul)
print("list_mul",list_mul)