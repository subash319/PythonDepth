# 9.  Rewrite this piece of code using ternary operator
#
# if bill_amount >2000:
#    free_home_delivery = 'Available'
# else:
#    free_home_delivery = 'Not Available'

bill_amount = int(input("Enter the bill amount:"))
free_home_delivery = 'Available' if bill_amount >2000 else 'NotAvailable'
print(f'free_home_delivery:{free_home_delivery}')