'''
tuple follows index, and comma separated values
tuple allows duplicate values
tuple is immutable
tuple we can create using of () but this is optional
empty tuple we can create ()
single value we can represent with comma
'''
# creating empty tuple
# t1 = ()
# # single value in tuple
# t1 =(10,)
# print(type(t1))
# # tuple allows + , * mathematical operators
# t2 = 2,13
# print(t1+t2)
# print(t2*3)
# # packing and unpacking tuples
# i,j,k = (3,4,5)
# print(j)
# x,y,z,a,b = 5,5,7,6,8 # this is unpacking
# a = x,y,z,a,b # this is packing
# print(a)
# print(a.count(5))
# print(a.index(7))
# print(len(a))
# print(min(a))
# print(max(a))
#
# t5 = (5,6,7)
# t6 = list(t5) # converting from tuple to list through type conversion
# print(type(t6))
# t6.append(8)
# print(t6)
# t6 = tuple(t6) # converting list to tuple
# print(type(t6))





def get_marksdata(marks):
    total = sum(marks)
    count = len(marks)
    average = total/count
    return total,count,average
data = (56,75,39,54,89,76)
sum_val,count_val,avg_val = get_marksdata(data)
print(f"total:{sum_val},count:{count_val},average:{avg_val}")





