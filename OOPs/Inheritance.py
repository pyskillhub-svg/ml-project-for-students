'''
Inheritance means we can use any class behaviour into another class is called a inheritance.
types of inheritance
1. single inheritance - one parent / one child class
2. multiple inheritance - multiple parent classes / child class
3. multi-level inheritance - sequence classes
4. Hirerchy inheritance - single parent / two child
5. Hybrid - inheritance - more than one inheritance we called it as a hybrid
'''


# single inheritance
# class Parent:
#     def house(self):
#         print("this property belongs to my son")
# class Child(Parent):
#     def my_house(self):
#         print("this house came from my father")
# son1 = Child()
# son1.house()

# multilevel - inheritance
# class Grand_parent:
#     def land(self):
#         print("this land is for my family property")
# class Parent(Grand_parent):
#     def car(self):
#         print("this car can be buy for my child")
# class Child(Parent):
#     def gift_assets(self):
#         print("i got car and land from my parents")
# son1 = Child()
# son1.land()

# multiple - inheritance

# class Father:
#     def land(self):
#         print("this land is for my son")
# class Mother:
#     def gold(self):
#         print("this gold is for my child")
# class Child(Father,Mother):
#     def wish(self):
#         print("good morning")
# child1 = Child()
# child1.land()
# MRO concept Method resolution order

#4. Hierarchical inheritance
# class Parent:
#     def property(self):
#         print("this property is for my two childs")
# class Child1(Parent):
#     def thanks(self):
#         print("i should say thanks to my parent ")
# class Child2(Parent):
#     def thanks(self):
#         print("I am thankfull to my parent")
# son1 = Child2()
# son1.property()

# Hybrid Inheritance -- means more than one inheritance
class Parent:
    def land(self):
        print("This is for my child")
class Child_wife:
    def gold(self):
        print("this gold is for my child")

class Child(Parent):
    def thank_Myfather(self):
        print("Thank you father")

class Grand_child2(Child,Child_wife):
    def thanks(self):
        print("thanks you father")

Grand_daughter = Grand_child2()
Grand_daughter.gold()
child2 = Child()
child2.land()

# advantages of Inheritance
'''
1.code reusability
2.Duplicate code removal
3. easy to add new features
4. need to less development.
5. easy to maintain
'''
# Dis advantages
'''
super class and sub classes are independent to each other
'''

