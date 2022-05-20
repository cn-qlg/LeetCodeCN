"""
给定两个时间，计算差的天数
"""
from datetime import datetime


def diff(t1, t2):
    t1 = datetime(*t1)
    t2 = datetime(*t2)
    return (t2-t1).days


"""判断是否是闰年
"""


def isRunYear(y):
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        return True
    return False


def diff2(t1, t2):
    # if t1[0] == t2[0] and t1[1] == t2[1]:
    #     return t2[2]-t1[2]

    isNegitave = False
    if t1[0] > t2[0] or (t1[0] == t2[0] and t1[1] > t2[1]) or (t1[0] == t2[0] and t1[1] == t2[1] and t1[2] > t2[2]):
        isNegitave = True
    if isNegitave:
        t1, t2 = t2, t1
    y = t2[0]-t1[0]
    t = 0

    # 整年情况
    for i in range(1, y):
        cy = t1[0] + i
        if isRunYear(cy):
            t += 366
        else:
            t += 365

    # 当前年剩余天数
    for i in range(t1[1], 13):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            t += 31
        elif i == 2:
            if isRunYear(t1[0]):
                t += 29
            else:
                t += 28
        else:
            t += 30
    t -= t1[2]

    # 计算目标年天数
    for i in range(1, t2[1]):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            t += 31
        elif i == 2:
            if isRunYear(t2[0]):
                t += 29
            else:
                t += 28
        else:
            t += 30
    t += t2[2]

    if t1[0]== t2[0]:
        if isRunYear(t1[0]):
            t -=366
        else:
            t -= 365

    if isNegitave:
        return -1 * t

    return t


# print(diff([2022,5,22], [2023,6,20]))
# print(diff2([2022,5,22], [2023,6,20]))

# print(diff([2022,5,22], [2021,6,20]))
# print(diff2([2022,5,22], [2021,6,20]))

# print(diff([2020,1,22], [2021,1,22]))
# print(diff2([2020,1,22], [2021,1,22]))

# print(diff([2022, 1, 1] ,[2022, 1, 10]))
# print(diff2([2022, 1, 1] ,[2022, 1, 10]))


# ---------------------
print(diff([2022, 1, 1], [2022, 1, 10]))
print(diff2([2022, 1, 1], [2022, 1, 10]))

print(diff([2022, 1, 1], [2022, 3, 10]))
print(diff2([2022, 1, 1], [2022, 3, 10]))

print(diff([2022, 1, 30], [2022, 3, 1]))
print(diff2([2022, 1, 30], [2022, 3, 1]))

print(diff([2000, 1, 1], [2000, 2, 10]))
print(diff2([2000, 1, 1], [2000, 2, 10]))

print(diff([2000, 2, 10], [2000, 3, 1]))
print(diff2([2000, 2, 10], [2000, 3, 1]))

print(diff([2000, 1, 10], [2000, 8, 20]))
print(diff2([2000, 1, 10], [2000, 8, 20]))

print(diff([2001, 1, 1], [2003, 3, 1]))
print(diff2([2001, 1, 1], [2003, 3, 1]))

print(diff([2001, 2, 2], [2003, 3, 3]))
print(diff2([2001, 2, 2], [2003, 3, 3]))

print(diff([1999, 1, 1], [2001, 3, 1]))
print(diff2([1999, 1, 1], [2001, 3, 1]))

print(diff([2000, 1, 1], [2003, 3, 1]))
print(diff2([2000, 1, 1], [2003, 3, 1]))

print(diff([2000, 2, 1], [2003, 3, 1]))
print(diff2([2000, 2, 1], [2003, 3, 1]))

print(diff([2000, 3, 1], [2003, 3, 1]))
print(diff2([2000, 3, 1], [2003, 3, 1]))

print(diff([1998, 1, 1], [2000, 1, 10]))
print(diff2([1998, 1, 1], [2000, 1, 10]))

print(diff([1998, 1, 1], [2000, 2, 10]))
print(diff2([1998, 1, 1], [2000, 2, 10]))

print(diff([1998, 1, 1], [2000, 3, 10]))
print(diff2([1998, 1, 1], [2000, 3, 10]))
