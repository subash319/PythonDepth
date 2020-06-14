# 10. Write a program to find whether a list contains any duplicate value.

find_list = [1,2,3,4,5,6,7,8,2]
for i in range(len(find_list)):
    if find_list.count(find_list[i]) > 1:
        print("List contains duplicate value at index:", i)
        break
else:
    print("no duplicate found")
