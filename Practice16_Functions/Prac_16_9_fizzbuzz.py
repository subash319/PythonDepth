# 9. Write a function named fizzbuzz that takes an integer as argument and returns 'Fizz'
# if that integer is divisible by 3, returns 'Buzz' if it is divisible by 5 and returns 'FizzBuzz'
# if it is divisible by both 3 and 5, otherwise it returns the integer itself.
#
# Use you function fizzbuzz in the following code.
#


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


def func(x):
    for i in range(1, x + 1):
        print(fizzbuzz(i))


func(50)
