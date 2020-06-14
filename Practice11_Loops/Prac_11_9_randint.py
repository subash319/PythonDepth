 # 9. Create a randomised list of size 10, that contains random numbers in the
 # range 1 to 50. Use randint function from random module.

import random
random_list = list()
for i in range(0, 11):
    number = random.randint(1, 50)
    random_list.append(number)
print(random_list)
