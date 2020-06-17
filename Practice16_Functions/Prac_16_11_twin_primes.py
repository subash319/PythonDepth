# 11. If two consecutive odd numbers are both prime (e.g. (3,5) (17, 19)) then they are known as twin primes.
# Write a function that returns a tuple containing all twin primes in a given range.
# Use the is_prime function defined in question 5.

def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def twin_primes(rang):
    t = []
    for i in range(3, rang + 1):
        if is_prime(i) and is_prime(i + 2):
            t.append((i, i + 2))
    print(t)
    return t


print("twin_primes", twin_primes(50))
