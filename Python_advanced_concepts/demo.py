# add = lambda x,y : x+y , x*y
# print(add(4,5))

# map function we can apply for sequence
l1 = [1,2,3]
l2 = (4,5,6)
result = list(map(lambda x,y : x+y , l2,l1))
print(result)

from functools import reduce
t1 = ('p','y','k')
re = reduce(lambda x,y:x+y,t1)
print(re)