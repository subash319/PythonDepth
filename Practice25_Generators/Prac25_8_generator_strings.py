# 8. Write an infinite generator function that generates strings 'Jan', Feb', 'Mar', …… 'Dec'.


def gen_str():
    lst_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    index = 0
    while True:
        yield lst_months[index]
        if index == len(lst_months)-1:
            index = 0
        else:
            index += 1

months = gen_str()
for month in range(20):
    print(next(months), end=' ')