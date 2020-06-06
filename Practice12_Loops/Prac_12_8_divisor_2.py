# 8. Find the smallest divisor of a number greater than 1, using (i) a while loop (ii) for loop

num = int(input("Enter the number to find the smallest divisor other than 1:"))
# i = 2
# while i <= num:
#     if num % i == 0:
#         print(i, end=' ')
#         break
#     i += 1
# else:
#     print("Enter a valid number greater than 3")

# for i in range(2,num+1):
#     if num % i == 0:
#         print(i, end=' ')
#         break
# else:
#     print("Enter a valid number greater than 3")
i=2
while num %i!=0:
    i+=1
print("Smallest divisor is:",i)