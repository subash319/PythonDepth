# numbers = [1,2,3,4,5,6,7,8]
#
# Write method calls to perform the following operations on this list.
#
# 1. Add 100 at the end of the list
#
# 2. Add 200 in the beginning of the list
#
# 3. Add 150 at index 3
#
# 4. Add 12,13,14,15 at the end of the list in one step.
#
# 5. Delete element 5 from the list.
#
# 6. Delete the last element from the list
#
# 7. Delete the element at index 5
#
# 8. Delete the first element from the list
#
# 9. Delete all the elements of the list
#
# 10. listA = [20,30,40,50,60,70]
#
#       Using the del keyword delete the element at index 5.
#
# 11. listA = [20,30,40,50,60,70]
#
#       Using the del keyword delete the last 3 elements.
#
# 12. What is the difference between listA.clear() and del listA.
#
# 13. numbers = [98, 11, 22, 9, 6, 32, 5]
#
#       What is the value of this expression sorted(numbers)[2:4]
#
# 14. numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
#
#       Make a new list that contains the 5 largest numbers from this list.
#
#       ( You should get this list  [22, 32, 35, 39, 98]  )
#
# 15. numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
#
#       Make a new list that contains the 5 smallest numbers from this list.
#
#       ( You should get this list  [1, 4, 5, 6, 7]  )
#
# 16. numbers = [3,2,1,5,7,9]
#
#       Sort this list in reverse order.
#
# 17. Sort this list of strings based on their length.
#
#       fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']
#
# 18. Perform case insensitive sort on this list of strings.
#
#       fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']
#
# 19. listA = [4,3,2,6]
#
#       listA = listA.sort(reverse=True)
#
#       print(listA)
#
#       listB = [9,4,3]
#
#       listB = listB.append(5)
#
#       print(listB)
#
#       What will the above code print.
#
# 20. Find the second largest and third smallest elements from this list.
#
#       numbers = [4,3,5,6,1,7, 2, 9]
#
# 21. numbers = [1,2,3]
#
#       numbers.extend( [4,5,6] )
#
#       print( len(numbers) )
#
#       numbers.append( [7,8,9] )
#
#       print( len(numbers) )

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# 1. Add 100 at the end of the list
numbers.append(100)
print(numbers)
# 2. Add 200 in the beginning of the list
numbers.insert(0, 200)
print(numbers)
# 3. Add 150 at index 3
numbers.insert(3, 150)
print(numbers)
# 4. Add 12,13,14,15 at the end of the list in one step.
new_list = [12, 13, 14, 15]
numbers.extend(new_list)
print(numbers)
# 5. Delete element 5 from the list.
numbers.remove(5)
print(numbers)
# 6. Delete the last element from the list
numbers.pop()
print(numbers)
# 7. Delete the element at index 5
numbers.pop(5)
print(numbers)
# 8. Delete the first element from the list
numbers.pop(0)
print(numbers)
# 9. Delete all the elements of the list
numbers.clear()
print(numbers)
# 10. listA = [20,30,40,50,60,70]
#       Using the del keyword delete the element at index 5.
listA = [20, 30, 40, 50, 60, 70]
del listA[5]
print(listA)
# 11. listA = [20,30,40,50,60,70]
#
#       Using the del keyword delete the last 3 elements.

listA = [20, 30, 40, 50, 60, 70]
del listA[-3:]
print(listA)
# 12. What is the difference between listA.clear() and del listA.
# listA.clear() clears the elements in the list but we will have an empty list
# Whereas for del listA we won't have the empty list also, Entire list will be deleted
listA = [20, 30, 40, 50, 60, 70]
listA.clear()
print(listA)
listA = [20, 30, 40, 50, 60, 70]
del listA
# print(listA)
# 13. numbers = [98, 11, 22, 9, 6, 32, 5]
#
#       What is the value of this expression sorted(numbers)[2:4]
numbers = [98, 11, 22, 9, 6, 32, 5]
print(sorted(numbers)[2:4])  # My expectation [98,11,9,22,9,6,32,5]
# As sorted method returns a sorted copy of the list, the above statment returns the sorted only for index's 2 & 3
# My expectation is wrong, first it will get sorted [5,6,9,11,22,32,98] then 2 and 3 index will be printed which is
# 9 and 11


# 14. numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
#
#       Make a new list that contains the 5 largest numbers from this list.
#
#       ( You should get this list  [22, 32, 35, 39, 98]  )
numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
new_list = sorted(numbers)[-5:]
print(new_list)

# 15. numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
#
#       Make a new list that contains the 5 smallest numbers from this list.
#
#       ( You should get this list  [1, 4, 5, 6, 7]  )

numbers = [39, 4, 1, 98, 11, 35, 7, 22, 9, 6, 32, 5, 10]
new_list = sorted(numbers)[:5]
print(new_list)

# 16. numbers = [3,2,1,5,7,9]
#
#       Sort this list in reverse order.

numbers = [3, 2, 1, 5, 7, 9]
numbers.sort(reverse=True)# on this list
print(numbers)
print(sorted(numbers, reverse=True)) # if new list then this method

# 17. Sort this list of strings based on their length.
#
#       fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']

fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']
fruits.sort(key=len)
print(fruits)

# 18. Perform case insensitive sort on this list of strings.
#
#       fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']
fruits = [ 'banana', 'fig', 'Mango', 'pomegranate' , 'Apple']
#case_insenstive_list = sorted(fruits, key = str.lower)
case_insenstive_list = fruits.sort(key=str.lower)
print(fruits)

# 19.   listA = [4,3,2,6]
#
#       listA = listA.sort(reverse=True)
#
#       print(listA)
#
#       listB = [9,4,3]
#
#       listB = listB.append(5)
#
#       print(listB)
#
#       What will the above code print.

listA = [4, 3, 2, 6]
listA = listA.sort(reverse=True)
print(listA)# [6,4,3,2] # wrong # the output would be None
listB = [9, 4, 3]
listB = listB.append(5)# [9,4,3,5] # Wrong # The output would be None as this methods return None
print(listB)

# 20. Find the second largest and third smallest elements from this list.
#
#       numbers = [4,3,5,6,1,7, 2, 9]
numbers = [4, 3, 5, 6, 1, 7, 2, 9]
numbers.sort()
print(numbers)
print(f'The second largest number is:{numbers[-2]} and the third smallest element is {numbers[2]}')

# 21. numbers = [1,2,3]
#
#       numbers.extend( [4,5,6] )
#
#       print( len(numbers) )
#
#       numbers.append( [7,8,9] )
#
#       print( len(numbers) )
# What will be output

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(len(numbers))#6
numbers.append([7, 8, 9])
print(numbers)
print(len(numbers))#7