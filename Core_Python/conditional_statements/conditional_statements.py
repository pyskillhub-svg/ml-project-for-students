'''
if is true
else means false
'''

# if program
# num = int(input("enter number:"))
# if num >=0:
#     print("positive number")
# else:
#     print("negative number")
# # 3 numbers which no is big
# a = int(input("enter a value"))
# b = int(input("enter b value"))
# c = int(input("enter c value"))
# if a>b and a>c: # 5>4 and
#     print("a is big")
# elif b>c:
#     print('b is big')
# else:
#     print("c is big")
#
#
#
# # nested if program
# if a>b:
#     if a>c:
#         print("a is big")
#     else:
#         print("c is big")
# else:
#     if b>c:
#         print("b is big")
#     else:
#         print("c is big")

# indentation concept
# indentation must be >0 and the all statements must follow same line space.

# n = 6
# if n >0:
#     print("n is greater then zero")

# Sequential execution or statements
print("hello world welcome to python program")
a = 5
b = 6
print(a+b)
print("end of the addition program")

# conditional statements or decision-making statements.
# 1. simple if

'''syntax
if conditon:
    statement '''
a = 5
if a> 0:
    print("positive value or number")

if - else :

'''
syntax:
if condition:
    statement
else:
    statement
'''
number = int(input("enter number:"))

if number%2 ==0:
    print("entered num is even")
else:
    print("entered num is odd")

# nested if
'''
syntax
if condition:
    if condition:
        statements
else:
    statements
'''

person_age = int(input("enter person age"))
person_citizenship = input("enter citigenship")
if person_age >=18:
    if person_citizenship == 'India':
        print("he is eligible for vote casting")
    else:
        print("only indian people have right to vote")
else:
    print("not eligible for vote casting")

# if - elif -else or if - elif ladder

'''syntax
if condition:
    statement
elif condition:
    statement
elif condition:
    statement
    
else:
    statement
'''
# short hand if condition

'''
syntax
if condition: statement

'''
a = 5
if a>0:print("a is positive number")

# short hand if -else statement

'''
syntax:
statement if condition else statement
'''
a,b = 5,6
print("a is big") if a>b else print("b is big")



























