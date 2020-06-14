# 10.
#
# We saw this loop in the lecture on break, modify this so that all the non-prime (composite) numbers are also printed.
#
# for n in range(2,100):
#   isprime=True
#   for i in range(2,n):
#        if n%i == 0:
#            isprime = False
#            break
#   if isprime:
#      print(n)
# The output should be of this form.
#
# 2 is prime
#
# 3 is prime
#
# 4 is not prime, as 4 = 2*3
#
# 5 is prime
#
# 6 is not prime, as 6=2*3
#
# 7 is prime

for n in range(2,10):
  isprime = True
  for i in range(2,n):
       if n%i == 0:
           isprime = False
           print(f'{n} is not prime, as {n} = {i}*{n//i}')
           break
  if isprime:
     print(f'{n} is prime')