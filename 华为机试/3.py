m, n = input("").split()
m = int(m)
n = int(n)

arrs = []
for _ in range(m):
    arrs.append(input().split())

# m = 6
# n = 6
# arrs = [
#     ["1","1","1","1","1","1"],
#     ["1","5","1","1","1","1"],
#     ["1","1","1","1","1","1"],
#     ["1","1","1","1","1","1"],
#     ["1","1","1","1","1","1"],
#     ["1","1","1","1","1","5"]
# ]

# arrs = [
#     ["1", "1", "1", "1", "1", "1"],
#     ["1", "5", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "5", "1"],
#     ["1", "1", "1", "1", "1", "1"]
# ]


def findAllEdges(arrs, m, n, i, j):
    edges = []
    if i - 1 >= 0:
        if j-1 >= 0 and arrs[i-1][j-1] != "5":
            edges.append(f"{i-1}-{j-1}")
        if arrs[i-1][j] != "5":
            edges.append(f"{i-1}-{j}")
        if j + 1 < n and arrs[i-1][j+1] != 5:
            edges.append(f"{i-1}-{j+1}")
    if j-1 >= 0 and arrs[i][j-1] != "5":
        edges.append(f"{i}-{j-1}")
    if j + 1 < n and arrs[i][j+1] != 5:
        edges.append(f"{i}-{j+1}")
    if i + 1 < m:
        if j-1 >= 0 and arrs[i+1][j-1] != "5":
            edges.append(f"{i+1}-{j-1}")
        if arrs[i+1][j] != "5":
            edges.append(f"{i+1}-{j}")
        if j + 1 < n and arrs[i+1][j+1] != 5:
            edges.append(f"{i+1}-{j+1}")

    return edges


index = 0

nodes = dict()

for i in range(m):
    for j in range(n):
        if arrs[i][j] == "5":
            edges = findAllEdges(arrs, m, n, i, j)
            # print(i, j, edges)
            isFound = False
            for edg in edges:
                if edg in nodes:
                    isFound = True
                    break
            if not isFound:
                index += 1
            for edg in edges:
                nodes[edg] = index


# print(nodes)

while True:
    indexs = set(nodes.values())
    for idx in indexs:
        connected = set()
        for k, v in nodes.items():
            if v == idx:
                i,j = k.split("-")
                edges = findAllEdges(arrs,m,n,int(i),int(j) )
                for edg in edges:
                    if edg in nodes and nodes[edg] != idx:
                        connected.add(nodes[edg])
        for k, v in nodes.items():
            if v in connected:
                nodes[k] = idx   
    after_indexs = set(nodes.values())
    if len(indexs) == len(after_indexs):
        break

# for idx in range(1, index+1):
#     connected = set()
#     for k, v in nodes.items():
#         if v == idx:
#             i,j = k.split("-")
#             edges = findAllEdges(arrs,m,n,int(i),int(j) )
#             for edg in edges:
#                 if edg in nodes and nodes[edg] != idx:
#                     connected.add(nodes[edg])
#     for k, v in nodes.items():
#         if v in connected:
#             nodes[k] = idx         
    # print(nodes) 
    # print("-----------------")          

print(len(set(nodes.values())))