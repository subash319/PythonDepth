# 5. Write a function is_prime that takes in an integer and returns True if the argument is prime,
# otherwise returns False.

def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True
print(is_prime(13))