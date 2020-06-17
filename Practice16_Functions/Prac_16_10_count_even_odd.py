# 10. Write a function that takes in a list of integers and returns the number of even and odd numbers from that list.

def count_even_odd(list_count):
    even_count,odd_count = 0,0
    for num in list_count:
        if num%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count,odd_count


print(count_even_odd(list(range(20))))