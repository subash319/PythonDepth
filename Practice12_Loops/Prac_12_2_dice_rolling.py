# 2. Write a program that simulates dice rolling. Use randint from random module.

import random
done = True
while True:
    roll = random.randint(1,6)
    print(roll)
    done = bool(input("Do you want to one more role, enter-continue, anything-quit"))
    if done:
        break