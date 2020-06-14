# L1  = ['China', 'Brazil', 'India', 'Iran', 'Iraq', 'Russia']
# L2  = ['Italy', 'Japan', 'China', 'Russia', 'Nepal', 'France']
# Write a program that inserts all common items of these 2 lists into a third list L3.

L1  = ['China', 'Brazil', 'India', 'Iran', 'Iraq', 'Russia']
L2  = ['Italy', 'Japan', 'China', 'Russia', 'Nepal', 'France']
L3 = list()
for country1 in L1:
    for country2 in L2:
        if country1 == country2:
          L3.append(country1)
print(L3)
