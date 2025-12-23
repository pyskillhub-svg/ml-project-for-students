'''
class & object
methods, modules, packages
polymorphism - method overriding, method overloading
Inheritance - single, multiple, multi-level, hierarchy, hybrid`
abstraction
decorator, generators
error handling try and except , finally, else, file handling
'''
# class is a blue-print and object is a real entity.
'''
customer id , customer name, customer address
'''

# using of class keyword we can create class.
# if we can write function in side class we call it as a method
# by default self constructor is there
# in class 3 types of variables will be there 1.local, 2.global 3.class
class Student:
    def display(self,name,age,course):
        print(f"student name {name} and age is {age} and course is {course}")

s1 = Student
print(s1)
s1.display('siva',35,'Python')















