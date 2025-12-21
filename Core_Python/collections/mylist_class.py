'''
a list is a comma separated values in []
list allows duplicates
list is a mutable modification supported (add, delete, update reassign )
list follows index, slicing supported
list() using of this we can do type casting
list allows homogeneous as well as heterogeneous.
list is a ordered collection
'''
# creating empty list
mylist = []
mylist1 = list()
print(mylist,mylist1)

#creating list
mylist2 = [2,3,4,56,1,12,2,3] # homogeneous datatype
mylist3 = [ 3,True, 'Python',4.5,5+9j]
print(mylist2)
print(mylist3)

# accessing elements in the list
# using of index we will get list values
l1 = [2,1,3,4]
print(l1[3])

# slicing means some portion of the data
# only start
print(l1[0:])
# only stop
print(l1[:5])
# only start and stop
print(l1[0:3])
# only step
print(l1[::2])
# reverse list
print(l1[::-1])

# adding methods 1) append() 2)extend 3 insert
# append() we can add only one value , that value will be stored at the end the list
fruits = ['apple','Mango','Watermelon']
print(fruits)
fruits.append('banana')
print(fruits)

# extend() using of this we can add multiple values at a time
fruits.extend(['grapes','orange','lemon'])
fruits2 = ['Musambbi','Guvva']
fruits.extend(fruits2)
print(fruits)

# insert method
fruits.insert(0,'Muskmelon')
print(fruits)

# updating methods  = operator for update purpose

fruits[2] = 'Berry'
print(fruits)

# remove methods in list pop(), POP(index), del, clear, remove
# pop() by default it will remove end value or last value in the list.
fruits.pop() # without passing index position
print(fruits)
fruits.pop(2) # passing index position
print(fruits)

# remove() : it will remove first occurrence value in the list
fruits.remove('banana')
print(fruits)

del fruits[3]
print(fruits)

del fruits # it will remove entire list including variable also
# print(fruits)

fruits.clear() # it will clear all values but not deleted the variable
print(fruits)

# information methods
flowers = ['rose','lilly','Jasmine','rose','Marigold','Lavender']
print(flowers.count('rose'))

# sorting method
numbers = [12,35,14,67,28,91,17]
numbers.sort()
print(numbers)

# inside the sort function by default reverse is false

numbers.sort(reverse=True)
print(numbers)

# reverse() it will reverse the list
numbers.reverse()
print(numbers)

# copy()

num = numbers.copy()
print(num)
print(id(numbers))
print(id(num))

# = means it will clone another variable refer same data location
numbers2 = numbers
print(numbers2)
print(id(numbers))
print(id(numbers2))

numbers2.append(45)
print(numbers)


# mathematical operation in list
l1 = [3,2,45,5]
l2 = ['rose','jasmine','lavender']
print(l1+l2) # concatenation
print(l1*3) # repetition

# membership operators in not in
print(3 in l1)
print(45 not in l1)

# loops in list

l3 = [45, 36,78,12,39,32,16]
for i in l3:
    if i%2 == 0:
        print(i)

l4 = ['python', 45, 36,32, 'java']

for i in l4:
    if type(i) == str:
        print(i)

for i in range(len(l4)):
    print(i,"index value is ",l4[i])

# nested lists : a list inside another list
# 2d list
nes_list = [[2,3],
            [4,5],
            [6,7]
            ]
print(nes_list[0][1])

nes_list1 = [[1,2,3,4],[2,3,4,5],[6,5,3,2]]
print(nes_list1[-1][-4])












