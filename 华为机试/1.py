def switch_class(class_id):
    if class_id == 1:
        return 2
    return 1

line = input("")
# line = "1/N 2/Y 3/N 4/Y"

children = line.split()

classes = {
    1:[],
    2:[]
}


pre = 1
min_num = 1000 # 小朋友最小编号
min_class = 1 # 最小编号小朋友所在班级

for child in children:
    num, yn = child.split("/")
    if yn == "N":
        pre = switch_class(pre)
    classes[pre].append(num)
    if int(num) < min_num:
        min_num = int(num)
        min_class = pre

for v in sorted(classes[min_class]):
    print(v, end=" ")
print()
for v in sorted(classes[switch_class(min_class)]):
    print(v, end=" ")
print()
