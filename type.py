# type.py

# string reverse

import sys

a = "I want a girl friend please"

def reverse(n):
    if n < 0:
        return
    sys.stdout.write(a[n])
    reverse(n-1)
    if n==0:
        sys.stdout.write("\n")
    sys.stdout.write(a[n])     

reverse(len(a)-1)
sys.stdout.write("\n")