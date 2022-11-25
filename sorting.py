l = [0,4,6,7,2,1,9]

#-------------Selection sort-------------
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] < l[j]:
#             l[i],l[j] = l[j],l[i]
# print(l)

# -------------Bubble sort--------------
# swap = False
# while not swap:
#     swap = True
#     for i in range(0,len(l)-1):
#         if l[i] > l[i+1]:
#             swap = False
#             l[i],l[i+1] = l[i+1],l[i]
# print(l)

# swap = False
# while not swap:
#     swap = True
#     for i in range(0,len(l)-1):
#         if l[i] > l[i+1]:
#             swap = False
#             l[i],l[i+1] = l[i+1],l[i]
# print(l)

#---------Insertion Sort----------------
# for i in range(1,len(l)):
#     k = l[i]
#     c = i-1
#     while k < l[c] and c>=0:
#         l[c+1] = l[c]
#         c -= 1
#     l[c+1] = k
# print(l)