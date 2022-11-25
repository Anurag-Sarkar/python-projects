a = [[1,2],[3,4],[5,6]]
b = [[6,5],[4,3],[2,1]]
r = []
for i in range(len(a)):
    q = []
    for j in range(len(a[0])):
        q.append(a[i][j]+ b[i][j])
    r.append(q)

print(r)

# a = [[1,2],[3,4]]
# b = [[6,5],[4,3]]
# r = []
# res = 0
# for i in range(len(a)):
#     q = []
#     res = 0
#     for j in range(len(a[0])):
#         res += a[i][j]*b[i][j]
#         q.append(res)
#     r.append(q)
# print(r)