# 6. Write a function that returns factorial of a number.

def factorial(num):
    fact = 1
    return fact if num == 0 else num*factorial(num-1)

print(factorial(5))