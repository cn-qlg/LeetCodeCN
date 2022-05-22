"""
f(0) = 1
f(1) = 1
f(2) = 1
f(3) = 2
"""
def f(n):
    if n <= 2:
        return 1
    p, q, r = 1, 1, 0
    for _ in range(2, n):
        r = p + q
        p, q = q, r
    return r

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))