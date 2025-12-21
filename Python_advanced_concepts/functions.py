'''
function is a block of code oor group of statements
we can create functions for code reusable purpose.
3 types
1. built-in functions
2. user defined functions or custom functions
3. anonymous functions using of lambda keyword we can create these functions

using of def keyword we can create function have two parts
1) function definition or declaration or creation
2) function calling or functon invoking

function have return statement and print option

function have arguments 1) default, 2) positional 3) keyword 4) arbitrary *args and **kwargs
function have variables 1) local variables means inside function 2) global variables means outside function

syntax:
def function_name():  # this is called function declaration or definition
    statements

function_name() # this is called function calling
'''
from functools import reduce


# def wish(): # function creation
#     print("good morning")
# wish() # function calling

# how many ways we can create functions
'''
1. function does not take any arguments and no return value.
2. function does not take any arguments and return value.
3. function take arguments and no return value.
4. function take arguments and return value.
'''
# 1 . no arguments and no return value.

# def greetings():
#     print("Advanced happy new year to all my students!")
# greetings()

# 2. no arguments and return value

# def greetings1():
#     return "advance happy new year wishes to all my students"
# print(greetings1())

# taking arguments and no return value
# def addition(a,b):
#     print(a+b)
# addition(8,6)

# taking arguments and return value
# def addition1(i,j):
#     return i+j
# print(addition1(8,5))

# variables local variables and global variables
# variables declaration
# scope of the variables local we can access only inside that function, global we can access entire any function of that file
# a = 10 # this is called global variable
# def sub(): # this we can call it as a parameters
#     b = 5 # this called local variables
#     return a-b
# print(sub()) # this we call it as a arguments
#
# def mul():
#     c = 4
#     return c*a
# print(mul())

# if local and global variables same name

# i = 6
# def sum1():
#     i = 10
#     print(i)
# sum1()
# print(i)

# how many ways we can create global variables
'''
1. outside function
2. inside function using of global keyword
3. without indentation we can create global variable.
'''
# x = 6
# def add():
#     global y
#     y = 5
#     return x+y+z
# z = 9
# k = 12
# print(add())

# arguments and parameters in functions
# 1. positional arguments 2. keyword arguments


# positional arguments

# def emp_info(name,age,salary):
#     print(f"my name is {name} and age is {age} and my salary is {salary}")
#
# emp_info(50000,'siva',34)

# keyword arguments
# def stu_info(stu_name,age,course):
#     return f"my name is {stu_name},age is {age} and course is {course}"
# print(stu_info(age = 26,stu_name= 'siva',course = 'Python Fullstack'))

# default arguments

# def stu_info1(name,age,roll_no='00001'):
#     print(f"my name is {name} and age is {age} and no is {roll_no}")
#
# stu_info1(name='sikandar',age = 23,roll_no='000023')

'''
1 positional always follow keyword and next default arguments
2. after keyword not possible to declare positional or else positional never come after keyword arguments.
'''

# def func(a,b,c):
#     print(a,b,c)
# func(10,20,15)
# func(b=20,c=14,a=45)
# func(30,20,c=30) # error
# func(20,b=15,c=25)
# func(50,15,c=45)

#  *args
# def result(*marks):
#     print(marks)
#     print(sum(marks))
# result(78,86,49,86,56,75)

# **kwargs
# def student_info(**info):
#     print(info)
# student_info(name='rajesh',age=26,roll_no='0000012',course='Python Testing')

# fixed positional data only

# def emp_info(name,age,/,*marks,course='python',gender):
#     print(f"my name is {name} and age is {age} and gender is {gender} and my course is {course} and my marks {marks}")
# emp_info('siva',25,78,46,76,45,course='Java',gender = 'male')
#
# # after * symbol all will consider as a keyword arguments
#
# def emp_info1(*marks,gender,course):
#     print(marks)
#     print(f'gender is {gender} and course is {course}')
# emp_info1(78,45,56,gender='male',course='Java')

# positional ,default,*, keyword **kwargs

'''
function creation
    statements
function calling
function have 2 types of variables 1) local 2 global
4) function we can create 4 ways
1) function with no arguments and no return statement
2) function with arguments and no return statement
3) function with no arguments and return statement
4) function with arguments and return statement

#arguments 
1) positional arguments
2) keyword arguments
3) default arguments
4) arbitrary arguments * args , **kwargs
'''





















