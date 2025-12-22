'''
Recursive function means a function tha calls itself during its execution,
1) base / termination case
2) recursive case or condition
'''
# factorial program
# def factorial_num(n):
#     if n == 0 or n == 1: # base case
#         return 1
#     return n*factorial_num(n-1) # recursive condition
# print(factorial_num(5))

# Closure
'''
a closure is a function that remembers and has access to variables fom its enclosing scope.
1. closure will work only in nested functions.

'''
# closure function program
def outer_func():
    message = 'Good morning'
    def inner_func(name):
        print(f"{message},{name}")
    inner_func('Nell')

outer_func()

def Out_func():
    i = 8
    def inn_func():
        j  = 4
        print(i+j)
    inn_func()
Out_func()
'''
advantages
1. to avoid multiple users can use variables.
2. for security of the defined data or values.
'''







