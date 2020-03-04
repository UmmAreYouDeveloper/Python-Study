# ex2.py

i = 0
s = 0
while i <= 1000:
    i += 1
    if i % 3: 
        continue
    else: 
        s += i

print(s,end=' ')