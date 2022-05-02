def count(s):
    res = ""
    pre = s[0]
    cnt = 0
    for c in s:
        if c == pre:
            cnt += 1
        else:
            res += f"{cnt}{pre}"
            pre = c
            cnt = 1
    res += f"{cnt}{pre}" 
    return res

# print(count("1"))
# print(count("11"))
# print(count("21"))
# print(count("1211"))

n = int(input(""))

a = "1"
for _ in range(n):
    a = count(a)

print(a)


