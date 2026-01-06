'''
if the class contains more than one method has same name
the method contains different datatypes of parameters or different no of parameters or both is called method overloading
ex:

# same method with different types of datatype
class A:
    def add(int,int):
        pass
    def add(str,str):
        pass
    def add(float,float):
        pass
obj1 = A()
obj1(2,3)
obj1('hi','hello')

# 2.same method with different no of parameters
class B:
    def method(self,int):
        pass
    def method(self,int,int):
        pass
    def method(self,int,int,int):
        pass
# same method has both different number of paramters & different datatypes
class C:
    def method(self,int,int):
        pass
    def method(self,str,str,str):
        pass
    def method(self,float,float,float,float):
        pass
Note Multiple dispatch using of this module we can write method overloading
'''
import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b
obj1 = A()
print(obj1.add('4','5'))

class B:
    def add(self,*args):
        if args:
            sum = type(args[0])()
            for i in args:
                sum+=i
            return sum

obj = B()
print(obj.add('a','b','c'))
# print(obj.add(4,5,6,7,8))
a=str()
print(type(a))



















