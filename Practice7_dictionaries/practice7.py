# PyDev console: starting.
# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
# s = 'Ideas are easy, execution is hard.'
# s[:5]
# 'Ideas'
# s[:-5]
# 'Ideas are easy, execution is '
# s[-5:]
# 'hard.'
# s[4]
# 's'
# s[-1]
# '.'
# s[::-1]
# '.drah si noitucexe ,ysae era saedI'
# s[:-1]
# 'Ideas are easy, execution is hard'
# s[:-5]
# 'Ideas are easy, execution is '
# s[4:]
# 's are easy, execution is hard.'
# s[5:]
# ' are easy, execution is hard.'
# s[100]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# IndexError: string index out of range
# s[-40]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# IndexError: string index out of range
# s[6:100]
# 'are easy, execution is hard.'
# s[-40:5]
# 'Ideas'
# s1 = s[:]
# s1
# 'Ideas are easy, execution is hard.'
# s2 = s1[:-3]
# s2
# 'Ideas are easy, execution is ha'
# s[5:5]
# ''
# S[4:14:2]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'S' is not defined
# S[4:14:2]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'S' is not defined
# s[4:14:2]
# 'saees'
# s[-1:0]
# ''
# s[-1]
# '.'
# a= 'Hello Worls'
# a= 'Hello World'
# a
# 'Hello World'
# a[-1]
# 'd'
# a[-1]+a[1:-1]+a[0]
# 'dello WorlH'
# L  = list(range(100,0,10))
# L
# []
# L  = list(range(100,0,-10))
# L
# [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
# L  = list(range(0,100,10))
# L
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# clear
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'clear' is not defined
# currency = dict()
# currency{'India' : 'Rupee','UK' : 'Pound','Japan' : 'Yen', 'Austria' : 'Euro', 'Bangladesh' : 'Taka'}
#   File "<input>", line 1
#     currency{'India' : 'Rupee','UK' : 'Pound','Japan' : 'Yen', 'Austria' : 'Euro', 'Bangladesh' : 'Taka'}
#             ^
# SyntaxError: invalid syntax
# currency{'India' : 'Rupee'}
#   File "<input>", line 1
#     currency{'India' : 'Rupee'}
#             ^
# SyntaxError: invalid syntax
# currency= {'India' : 'Rupee'}
# currnecy
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'currnecy' is not defined
# currency
# {'India': 'Rupee'}
# currency = {'India' : 'Rupee','UK' : 'Pound','Japan' : 'Yen', 'Austria' : 'Euro', 'Bangladesh' : 'Taka'}
# currency
# {'India': 'Rupee', 'UK': 'Pound', 'Japan': 'Yen', 'Austria': 'Euro', 'Bangladesh': 'Taka'}
# del currency['UK']
# currency
# {'India': 'Rupee', 'Japan': 'Yen', 'Austria': 'Euro', 'Bangladesh': 'Taka'}
# c= pop['UK']
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'pop' is not defined
# c= currency.pop('UK')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: 'UK'
# c= currency.pop('Japan')
# c
# 'Yen'
# currency
# {'India': 'Rupee', 'Austria': 'Euro', 'Bangladesh': 'Taka'}
# currency.popitem()
# ('Bangladesh', 'Taka')
# currency = {'Switzerland':'Swiss Franc'}
# currency['India'] = 'Indian Rupee'
# currency
# {'Switzerland': 'Swiss Franc', 'India': 'Indian Rupee'}
# currency.keys()
# dict_keys(['Switzerland', 'India'])
# currency.values()
# dict_values(['Swiss Franc', 'Indian Rupee'])
# currency.items()
# dict_items([('Switzerland', 'Swiss Franc'), ('India', 'Indian Rupee')])
# fruits_prices =  { 'apple': 100, 'banana':75, 'mango':80 }
# fruits_prices.get('apples',20)
# 20
# fruits_prices
# {'apple': 100, 'banana': 75, 'mango': 80}
# fruits_prices.get('grapes',0)
# 0
# fruits_prices
# {'apple': 100, 'banana': 75, 'mango': 80}
# fruits_prices.getmethod('grapes',0)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'getmethod'
# fruits_prices.setdefault('apples',0)
# 0
# fruits_prices.setdefault('grapes',0)
# 0
# fruits_prices
# {'apple': 100, 'banana': 75, 'mango': 80, 'apples': 0, 'grapes': 0}
# del fruits_prices['apples']
# fruits_prices
# {'apple': 100, 'banana': 75, 'mango': 80, 'grapes': 0}
# del fruits_prices['apple']
# fruits_prices
# {'banana': 75, 'mango': 80, 'grapes': 0}
# fruits_prices.setdefault('apple',100)
# 100
# fruits_prices
# {'banana': 75, 'mango': 80, 'grapes': 0, 'apple': 100}
# fruits_prices.setdefault('apple',0)
# 100
# fruits_prices
# {'banana': 75, 'mango': 80, 'grapes': 0, 'apple': 100}
# login = {}
# names = ['John', 'Sam', 'Marie', 'Anne']
# login.fromkeys(names,None)
# {'John': None, 'Sam': None, 'Marie': None, 'Anne': None}
# login
# {}
# login
# {}
# login.fromkeys(names,None)
# {'John': None, 'Sam': None, 'Marie': None, 'Anne': None}
# login = login.fromkeys(names,None)
# login
# {'John': None, 'Sam': None, 'Marie': None, 'Anne': None}
# designation = ['programmer', 'manager', 'accountant']
# ...salary = [4000, 5000, 3000]
# two_lists = dict(zip(designation,salary))
# two_lists
# {'programmer': 4000, 'manager': 5000, 'accountant': 3000}
# two_lists = zip(designation,salary)
# two_lists
# <zip object at 0x000001B1163C4A80>
# two_lists = dict(zip(designation,salary))
# two_lists
# {'programmer': 4000, 'manager': 5000, 'accountant': 3000}
# python_books = [ 'Learn Python', 'Programming in Python', 'Python in depth']
# ...cplusplus_books = ['C++ in depth', 'C++ Programming']
# ...java_books = ['Java Programming', 'Learn Java']
# books = {'python':python_books, 'cplusplus':cplusplus_books, 'java':java_books}
# books
# {'python': ['Learn Python', 'Programming in Python', 'Python in depth'], 'cplusplus': ['C++ in depth', 'C++ Programming'], 'java': ['Java Programming', 'Learn Java']}
# books[python]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'python' is not defined
# books['python']
# ['Learn Python', 'Programming in Python', 'Python in depth']
# book_prices = {'Learn ABC':150, 'Learn 123': 200, 'Rhymes':300, 'Cursive Writing':250}
# ...new_stock = {'Stories':350, 'Poems':290, 'Spellings':200}
# book_prices.update(new_stock)
# book_prices
# {'Learn ABC': 150, 'Learn 123': 200, 'Rhymes': 300, 'Cursive Writing': 250, 'Stories': 350, 'Poems': 290, 'Spellings': 200}
# list_range = dict()
# list_range = fromkeys(range(1000,10000,1000),None)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'fromkeys' is not defined
# list_range.fromkeys(range(1000,10000,1000),None)
# {1000: None, 2000: None, 3000: None, 4000: None, 5000: None, 6000: None, 7000: None, 8000: None, 9000: None}
# student = {'name': {'first': 'John',
# ...                    'last': 'Mark'
# ...                    },
# ...           'marks': 98,
# ...           'age': 20
# ...           }
# student['name']['last']
# 'Mark'
# d = {2: 300, 8: 900, 7: 800, 1: 100}
# sorted(d.keys())
# [1, 2, 7, 8]
# marks =  {  2234 : [99,23,56],
# ...            2135 : [67,56,68],
# ...            2199 : [78,89,66]
# ...          }
# sum(marks['2135'])
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: '2135'
# marks['2135']
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: '2135'
# sum(marks[2135])
# 191
# { (0,5): 4,   (1,3):8,   (3,4):6,   (5,2):3  }
# {(0, 5): 4, (1, 3): 8, (3, 4): 6, (5, 2): 3}
# sparse_matrix = { (0,5): 4,   (1,3):8,   (3,4):6,   (5,2):3  }
# sparse_matrix
# {(0, 5): 4, (1, 3): 8, (3, 4): 6, (5, 2): 3}
# sparse_matrix[(1,2)]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# KeyError: (1, 2)
# sparse_matrix.get((1,2),0)
# 0
# sparse_matrix.get((2,0),0)
# 0
# sparse_matrix
# {(0, 5): 4, (1, 3): 8, (3, 4): 6, (5, 2): 3}