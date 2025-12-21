'''
1) function assign to variable
2) function as an arguments  or passing function as arguments
    ( this functions we can call higher-order functions)
3) function we can return in another function
4) functions we can store in data structures
5) run-time functions map, filter, reduce
6)Closure concept.
'''
from Python_advanced_concepts.return_statements import even_no


# function assign to a variable
def greetings(name):
    return f"Happy advance christmas wishes to you {name}"
wish = greetings
print(wish('Ronald'))

# function as an arguments or passing function as arguments

# def calculate(func,a,b):
#     return func(a,b)
# def add(i,j):
#     return i+j
# def mul(i,j):
#     return i*j
# print(calculate(add,7,8))
# sum_values = calculate(add,12,15)
# print(sum_values)
# print(calculate(mul,7,3))


# return a function from function
# def outer_func():
#     def inner_func():
#         return "Good morning"
#     return inner_func()
# print(outer_func())

# storing functions in data structures.
# list data structure
# def add(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# def subtraction(a,b):
#     return a-b
# def division(a,b):
#     return a/b


# a,b,c = 5,6
# list_operations = [add,mul,subtraction,division]
# for operation in list_operations:
#     print(operation(a,b))

# dictionary data structure
# commands = {'a':add,'m':mul,'s':subtraction,'d':division}
# command = 'a'
# if command in commands:
#     result = commands['a'](3,5)
#     print(result)

# runtime higher-order functions map, filter, reduce
# def sqr(x):
#     return x*x
# print(sqr(7))
#
# sqr = lambda x,y,z:x+y+z
# print(sqr(5,7,8))
# syntax
'''
function name = lambda arguments : expression

'''
# map function
'''
syntax 
function name = list(map(lambda arguments : expression, defined variable))
'''
l1 = [1,2,3,4]
l2 = [4,5,6,7]
l3 = [5,4,7,8,'thon']
sqr1 = list(map(lambda x :x*x,l1))
sum_lists = list(map(lambda x,y:x+y,l3,l2))
print(sqr1)
print(sum_lists)

# filter function
'''
syntax:
function name =filter(lambda arguments:expression,)
'''


l4 = [5,6,7,8,4,2,12,16,-4,-5,-3]


positive_no = tuple(filter(lambda i : i> 0,l4))
even_no = list(filter( lambda j : j%2 == 0 , l4))
print(positive_no)
print(even_no)

# reduce function
from functools import reduce
l5 = [4,5,6,7]
result = reduce(lambda x,y : x+y,l5)

print(result)







