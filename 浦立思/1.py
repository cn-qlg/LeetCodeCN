""" 
f(1) = 1
f(2) = 1
f(3) = 2
f(4) = 3
"""
def fb(n):
    if n <= 2:
        return 1
    a,b,c = 1,1,0
    for _ in range(2,n):
        c = a + b
        a,b = b, c
    return c

print(fb(2))
print(fb(3))
print(fb(4))
print(fb(5))