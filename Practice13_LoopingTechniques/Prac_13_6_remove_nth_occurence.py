# 6. Write a program to remove nth occurrence of an item from a list.
list_n = [1,2,3,4,2,2,2,4,5,6]
n = int(input("Enter the elemenet to remove an element from the list"))
c = int(input("Enter the which occurrence the element should be deleted"))
count = 0
for i,num in enumerate(list_n):
    if num == n:
        count += 1
        if count == c:
            list_n.pop(i)
            break
print(list_n)
