# 7. Print the names of unique cities from the following dictionary. The city names should be in all capitals.

D = {'Sam': 'Paris', 'Tom': 'London', 'Bob': 'Paris', 'Dev': 'Bareilly', 'Tim':'Paris', 'Raj':'London'}

for city in set(D.values()):
    print(city.upper())