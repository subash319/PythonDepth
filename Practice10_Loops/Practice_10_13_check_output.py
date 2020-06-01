# 13. This program is written for creating two lists evens and odds from the list numbers.
# But it does not give the correct output. Can you find what the problem is.

# only Immutable types can have declaration like that, so it forms tuple 
evens = []
odds = []
numbers = [10, 2, 3, 41, 5, 7, 8, 9, 62]
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(evens)
print(odds)