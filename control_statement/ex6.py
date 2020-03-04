# ex6.py

# list comprehension

''' original code
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
'''
numbers = [1, 2, 3, 4, 5]
result = [num *2 for num in numbers if num % 2 ==0]
print(result)