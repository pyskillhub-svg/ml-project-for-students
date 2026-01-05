'''
Poly many
morphism means forms
1. Operator level - operator over loading
2. function level
3. class level
4. polymorphism in Inheritance --- Inheritance overriding

1. compile time or static tim - when we can use operator or function its called compile time polymorphism
2. runtime or dynamic time - methods we call it as a runtime or dynamic time polymorphism
'''

# Operator level - operator overloading means changing the default behaviour or an operator depending on operand
# adding two integers , adding two strings ,adding two float values, adding two lists
# a = 40
# b = 5
# print(a+b)
# s1 = 'Python'
# s2 = 'Programming language'
# print(s1+s2)

# Function level polymorphism  len()
# l1 = ['Python','Programming','Language']
# print(len(s1))
# print(len(l1))

# Class level polymorphism
# class Car:
#     def move(self):
#         print("drive!")
# class Bike:
#     def move(self):
#         print("ride")
# class Plane:
#     def move(self):
#         print("Fly!")
# class Boat:
#     def move(self):
#         print('Sail!')
# car = Car()
# bike = Bike()
# boat = Boat()
# plane = Plane()
# for travel in (car,bike,boat,plane):
#     travel.move()

# Inheritance level polymorphism
class Parent:
    name = "Jhon"
class Child(Parent):
    name = 'Scott'
    def person_name(self):
        print(super().name)
c1 = Child()
c1.person_name()

class P:
    def display(self):
        print('This is parent class')
class C(P):
    def display(self):
        super().display()
        print("This is child class")
c2 = C()
c2.display()

