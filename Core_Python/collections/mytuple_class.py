'''
tuple is a immutable object or datatype in python.
tuple allows duplicates
tuple follows order , indexing , slicing also supported
tuple also allows homogeneous as well as heterogeneous datatypes.
we can represent tuples in () , this () is optional
'''

# creating empty tuple
t1 = ()
t2 = tuple()

print(t1,t2)

#  creating tuple with () parenthesis and without parenthesis

mytuple = (10,12,15,16,12) # with parenthesis and homogeneous data
mytuple1 = 'Python',True,15,-20,4.5,4+9j # without parenthesis and mixed data

print(type(mytuple))
print(type(mytuple1))

print(mytuple)

# single value in tuple, comma must

mytuple3 = (10,)
t3 = 12,
print(type(mytuple3))

# access elements in tuple index and slicing
using of indexing
print(mytuple[0])

# slicing
print(mytuple[:3])
print(mytuple[1:4:2])

# mathematical operations in tuple concatenation +, repetition *
t1 = (10,12,3)
t2 = (15,13)
# t3 = t1+t2
print(t1+t2) # concatenation
print(t2*3) # repetition

# membership operators in tuples in, not in
print(25 in t1)
print(25 not in t1)


# tuple methods  index, count
tuple5 = (12,4,12,5,16,17,12,19,32,23,43,56,54,12)
print(tuple5.index(12))
print(tuple5.index(12,7))
print(tuple5.count(12))

# difference between the list and tuple
'''
list is mutable , tuple is immutable
list is slower then compare to tuple
some sensitive data we can go with tuple. 
'''
# loops in tuple

tuple6 = (12,4,12,5,16,17,12,19,32,23,43,56,54,12)
for i in tuple6:
    if i%2 == 0:
        print(i)

tuple7 = 'python', True, 12,-7,'Ruby'
for i in range(len(tuple7)):
    print(f"{i} index value is {tuple7[i]}")

# tuple packing and unpacking
student_info = ('siva',25,'B.com','AGrade')
name, age, course,grade = student_info
print(course)

# *extended unpacking
student_result = ('rajesh',75,86,94,56,75,63,'B.Sc')
name, *marks,course = student_result
print(name) # rajesh
print(course)
print(tuple(marks))

# packing
name,age,course,grade = 'Ramesh',26,'B.Sc','Bgrade'
student_bio = name, age, course,grade
print(student_bio)

# tuple supported built-in functions, len(), max(), min(), sum(), Type(), id() etc

# any() and all() functions

t9 = True,False,False,0,False
t10 = True,1,True
print(any(t9))
print(all(t10))

# swapping using tuple

a = 3
b = 4
a,b = b,a
print(a,b)












