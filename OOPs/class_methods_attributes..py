'''
class : a class is a blueprint of the object. a class is a collection of attributes(variables) and methods.
class is never occupy any space in memory
object : real entity , physical entity
using of class we can create any no of objects.
a function inside class is a method.
basic methods are two 1) instance method, 2) static method
without object we cann't call instance methods
using of class we can call static methods @ static
syntax:
class calssname:
    methods:

obj = classname
obj1 = classname
'''
# creating class
# class Myclass1:
#     def m1(self):
#         pass
#     def m2(self):
#         print("Good Morning")
# obj1 = Myclass1()
# obj1.m1()
# obj1.m2()

# static method

# class Myclass2:
#     def m3(self):
#         print("Good morning")
#     @staticmethod
#     def m4():
#         print("Have a good day!")
# Myclass2.m4()

'''
variables or attributes
1. global attributes = means any variable outside the class.
2. class attributes = means we can define inside the class.
3. local attributes = we can define inside the method.
'''
# using class attributes

# class Calcu:
#     a,b=5,6 # class attributes
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def addition(self):
#         c = 6 # local attribute
#         return self.a+self.b+c
# myobj1 = Calcu()
# print(myobj1.addition())

# global attributes, class attributes and local attributes
# a,b = 12,15 # global attributes
# class Operations:
#     i,j = 6,5 # class attributes
#     def add(self):
#         c,d = 7,8 # local attributes
#         return c,d
#
#     def sub(self):
#         a,b = 7,8 # local
#         print(b-a)
#         print(globals()['b']-globals()['a'])
#         print(self.j-self.i)
#         print(d-c)
# obj3 = Operations()
# obj3.sub()

# any no of objects with single class.
'''
constructor() and method()
method() : method we can give any name.
method returns values
method can take arguments/parameters.
we have to use object to invoke the method

constructor():
constructor name is fixed. __init__
constructor also take arguments and parameters
constructor never return any value.
constructor will be called at the time of object creation itself.
'''


class Student:

    def __init__(self,name,id,mobile):
        self.name = name
        self.id = id
        self.mobile = mobile
        print("Good morning to all!")



    def student_info(self):
        print("How are you!")
        print(f"student name is {self.name}, id is {self.id} and mobile no is {self.mobile}")
mystudent = Student('Neel','000034',12345)
mystudent.student_info()
mystudent1 = Student('Ronald','000045',123231)
mystudent1.student_info()































