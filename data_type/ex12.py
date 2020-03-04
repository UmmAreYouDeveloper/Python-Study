# ex12.py

# copy

a = b = [1,2,3]
a[1] = 4
print(b)

'''
why change b second element
because a and b are same object
'''
'''
 technique for copy 
 a, b and c are different object
'''
# method 1
a = [1,2,3]
b = a[:]
a[1] = 4
print(b)
# method 2
from copy import copy
c = copy(b)
print(c)
