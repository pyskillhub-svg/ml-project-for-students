# format methods in strings
'''
to convert values (either no's str, float any other values ) to print meaningful way
most readable purpose
convenient to user understanding purpose
methods in string formating
--------------------------
1) percentage(%) starting onwards
2) format() 2.6 or 3 version onwards
3) f -strings available 3.6 onwards
'''

# percentage % %s means for strings purpose %d means digits any no's and finally %f means float no purpose
name = 'Rajesh'
age = 32
salary = 25000
# print('employee name is %s and age is %f and salary is %d'%(name,salary,age))
# print('%s developed in the year %d ' %('python',1991))

# using of format()
# print("{},{},{}".format(name,age,salary))

# positional format()
# print("my salary is {2},and i am {0},and my age is {1}".format(name,age,salary))

# keyword format()
# print("my name is {name} and age is {age} and salary is {salary}".format(name='siva',salary = 25000,age =32))

# alignment and padding concepts in format()
# print("{:>20}".format('rajesh'))
# print("{:^20}".format(name))
# print("{:.3f}".format(salary))

# f-string concepts
''' 
we can use either f or F
'''
print(f"my name is {name}")
# print(F"my age is {{{age}}}")
# print(f"my salary is {salary:.2f}")
print(f"my name is {name}, \n age is {age:^25} \n and salary is {salary:.2f}")