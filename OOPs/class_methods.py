from types import MethodType

class Employee:
    increment = 0.10
    def employee_info(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
        print(f"name is {self.name} and id is {self.id} and salary is {self.salary}")
    @classmethod
    def employee_increment(cls,salary):
        increment_salary = salary*cls.increment
        print(f'your incremented salary is {increment_salary}')

neel = Employee()
neel.employee_increment(50000)
neel.employee_info('Neel','000034',50000)
# print(neel.__dict__)
# del neel.id
print(neel.__dict__)
ronald = Employee()
ronald.employee_info('ronald','000035',50000)
# print(ronald.__dict__)

'''
create method outside class and assign to object
syntax
object.methodname = methodtype(function,object)
'''


# def emp_address(self):
#     print(f'employee address is bangalore}')
# neel.emp_address = MethodType(emp_address,neel)
#
# print(neel.__dict__)
# neel.emp_address()

# factory methods
import datetime
class Emp:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    @classmethod
    def getAgeAsDOB(cls,name,id,age):
        return cls(name,id,datetime.datetime.now().year-age)

emp1=Emp.getAgeAsDOB('siva','00002',1992)
print(emp1.name,emp1.id,emp1.age)