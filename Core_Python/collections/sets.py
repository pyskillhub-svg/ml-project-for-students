'''
set we can create using of {}
set never allows duplicates, its a unique values
set never follow index, unordered collection
empty set we can create using of set() function
set also allows multiple datatypes
'''

# creating empty set
s1 = set()

# creating set
s1 = {1,2,3,4,3,2,4}
print(s1)

# adding values to set add(), update()
# add() using of this method we can add only one value
s1.add(8)
# update method # using of this method we can add multiple elements at a time.
s1.update({4,8,9,7})
print(s1)

# removing methods in set remove(), discard(), pop(), clear()
# remove() # if element not there we will get Keyerror
s1.remove(7)
print(s1)
# discard() : if element not there never through error, if element is there it will removed.
s1.discard(7)
'''
if the value available in set remove function will remove that value, or else it will through error keyerror.
discard function if the value is there removed if value not there never through any error.
'''
# pop() randomly it will take value and removed
s1.pop()
print(s1)

# clear() : it will cleared all the elements but set will not removed, empty set will be there.
s1.clear()
print(s1)
del s1 # del keyword will remove entire set including elements, after this we will get name error.
print(s1)

# copying set
s2 = {1,4,3,2,6,9,8,7}
print(s2)
s3 = s2.copy()
print(s3)
# len(), min(),max(), id(), type() etc

# information providing methods issubset, issuperset, isdisjoint

set3 = {2,3,4,5,6,7,45}
set4 = {2,12,15}

print(set4.issubset(set3))
print(set3.issuperset(set4))
set5 = set3.isdisjoint(set4)
print(set5)



# mathematical functions
# 1) union it will return all common values from two sets | for union symbol
set1 = {1,2,3}
set2 = {4,3,5}
print(set1.union(set2))
print(set1 | set2)

# intersection it will return common values in both sets we can use & for intersection
print(set1.intersection(set2))
print(set1 &set2)

# intersection_update: remove the elements in this set that are not present in other specified set, &=
s1 = {10,11,12}
s2 = {14,13,12,15}
s1.intersection_update(s2) # s1&=s2
print(s1)
print(s2)


# difference() it will return the elements present in set1 but not in set2 we can use - symbol for difference
print(set1.difference(set2))
print(set1-set2)
# different_update : it will removes the elements in this set that are also included in another specified set '-='
s1 = {1,2,3,4}
s2 = {5,6,4,7,8}
s1.difference_update(s2) #
print(s1)

# symmetric difference it will return either elements presents in sets not return common values, ^
print(set1.symmetric_difference(set2))
print(set1^set2)

#Symmetric_difference_update: inserts the symmetric_differences from this set to another specified set , ^=
set6 = {1,2,3}
set7 = {3,2,8,7}
set6.symmetric_difference_update(set7)
print(set6)



# frozenset is immutable concept of set
# frozenset will support all information related methods, not possible to do any modification methods.
set1 = {1,2,34,4}
set2 = frozenset(set1)
set1.add(7)
#set2.add(5) # frozenset not supported modification methods



















