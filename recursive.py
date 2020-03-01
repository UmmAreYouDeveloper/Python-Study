# type.py

# string

a = "I want a girl friend please"

def reverse(n):
    if n < 0:
        return
    print(a[n])  
    reverse(n-1)
    print(a[n])        

reverse(len(a)-1)