import math

def msqrt(x):
    i = 1
    s = 0
    if x < 1:
        s = 0
    else:
        for i in range(1,x//2 + 1):
            if i**2 == x:
                return i
            elif i**2 > x:
                break
        s = i
        if i ** 2> x:
            s = i -1

    t = 1
    while t <=10:
        for _ in range(1, 10):
            s += 10 ** -t
            if s ** 2 == x:
                return s
            elif s ** 2 > x:
                break
        if s ** 2 > x:
            s -= 10 ** -t
        t += 1
    return s

print(msqrt(4), 4)
print(msqrt(2), math.sqrt(2))
print(msqrt(3), math.sqrt(3))
print(msqrt(9))
print(msqrt(0.25))