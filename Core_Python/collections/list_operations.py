"""
list is mutable object
list support homogeneous as well as heterogeneous datatypes
list we can represent using of [], with  comma separated value
list support typecasting
list allows duplicates
we can represent empty list with []
list follows index
"""

# creating empty list
mylist1 = []
print(mylist1)
# creating list and values adding to list
mylist = [1, 2, 3, 'neel']
# values adding to list methods append(), extend, insert() methods
# 1 append method using this method we can add one value and the value is added at the end of the lists
print(mylist)
#2.extend method, using of this we can add multiple values at a time
mylist1 = [3,4,5]
mylist.extend(mylist1) # adding multiple values mylist.extend([4,5,6])
print(mylist) # [1, 2, 3, 'neel', 3, 4, 5]
#3.insert method using of insert we can add value per a particular index position
mylist.insert(2,10)
print(mylist)

# remove methods pop(), remove(), clear()
# pop method # by default it will remove end of the value
mylist.pop()
print(mylist)
mylist.pop(2) # index based removing values
print(mylist)
#remove we need to pass value, if values are duplicates first one will be removed
mylist.remove(3)
print(mylist)
#clear method to clear all values from the list.
# mylist.clear()
print(mylist)

# information providing methods count(), index()
# 1.count method it wll give how many values for a particular
print(mylist.count(3))
# 2.index it will give value index position
print(mylist.index(3))

#  sorting methods ascending  and descending order
# sort method
l1 = [4,5,3,7,1]
l2 = sorted(l1)
print(l2) # we will get output of sorted list Ascending order
# reverse in sort () function by default reverse is False in sort function
l3 = [4,3,1,5,6,2,8]
l3.sort(reverse=True) # we will get descending order sort but sort by default id false
print(l3)
l3.sort(reverse=False)
print(l3)

# reverse() function, it will reverse the existing list.
l5 = [3,2,5,6,1,8]
l5.reverse()
print(l5) # output [8, 1, 6, 5, 2, 3]

# Mathematical operation in list +, * operations
# + operator

list1 = [2,3,4,5]
list2 = [8,7,3,2]
print(list1+list2) # [2, 3, 4, 5, 8, 7, 3, 2]

# * operator
print(list1*3) # [2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5]

# Built in functions, id(), type(), min(), max(), len() etc
my_list1 = [3,2,1,4,5,3,2,5,6,9,8]
print(type(my_list1)) # it will give which type object that
print(id(my_list1)) # it will give address of the lists
print(len(my_list1)) # it will give length of the list
print(min(my_list1)) # it will give minimum value in that list
print(max(my_list1)) # it will give maximum value in that list


# =, copy, shallow copy and deepcopy
# '=' operator it will create another object with same memory location
my_new_list = [4,3,8,2]
my_new_list1 = my_new_list
print(id(my_new_list))
print(id(my_new_list1))
print(my_new_list is my_new_list1)

# updating values in new list
my_new_list1[2] = 9 # updating new value behalf of 8  , this will also updated in old list
my_new_list1.append(12) # adding new value to the latest list, this will also added in old list
print(my_new_list1)
print(my_new_list)

# multi-dimensional list also will work same as single dimensional list when we can use assignment operator '='.

# copy method copy and shallow copy methods
'''
copy method will also work like shallow copy
syntax 
copy method
l1 = [1,2,3]
l2 = l1.copy() # copy() method
but if want to use shallow copy we need to import copy library
'''
import copy
list5 = [2,6,1,7]
list6 = copy.copy(list5) # shallow copy
list6[0] = 9 # updating new value in list6 but never updated in list5
print(list5)
print(list6)

list_shallow = [3,2,1,[4,5],6]
list_shallow1 = copy.copy(list_shallow)
list_shallow1[3][0] = 12 # here updating new value in inner list, so update will happen in old list also
print(list_shallow) # [3, 2, 1, [12, 5], 6]
print(list_shallow1) # [3, 2, 1, [12, 5], 6] updated value in two lists.

# Note in shallow copy only inner list values will save same location so update will happed in both lists inner list.

# deepcopy() : deepcopy will work as independently, when we can use deep copy new object will create with new memory location.
l1 = [1,2,3,[4,5]]
l2 = copy.deepcopy(l1)
print(l2)
print(l1)
print(l1 is l2)
l2[3][0] = 8
print(l2)
print(l1)

'''
= we can go with when we want change both the objects. 
copy.copy() : shallow copy if we want to change outer list with out effect original we can go with this shallow copy
deep copy we want to new object and to make changes in that new object we can go with this deep copy.
'''
















