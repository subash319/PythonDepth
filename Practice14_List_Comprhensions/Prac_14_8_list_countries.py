 # 8. Given this dictionary where country name is the key and currency name is the value,
 # how will you find the name of the country whose currency is 'Yen'.

# Create a list of countries that have 'Euro' as the currency.

d = {   'India' :  'Rupee',
        'UK' : 'Pound',
        'France':'Euro',
        'Japan' : 'Yen',
        'Austria' : 'Euro',
        'Bangladesh': 'Taka',
        'Italy' : 'Euro'
     }
d_new = [country for country, currency in d.items() if currency == 'Euro']
print(d_new)
