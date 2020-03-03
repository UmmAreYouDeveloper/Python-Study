# ex9.py

# error detect

a = dict()

# case1
a['name'] = 'python'
# case2
a[('a',)] = 'python'
'''
# case 3 -> this is error because key is list
a[[1]] = 'python'
'''
# case 4
a[250] = 'python'
print(a)