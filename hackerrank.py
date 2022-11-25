# l = []
# for i in range(int(input())):
#     x = [i if i.isalpha() else int(i) for i in input().split()]
#     if x[0] == "insert":
#         l.insert(x[1],x[2])
#     elif x[0] == "append":
#         l.append(x[1])
#     elif x[0] == "print":
#         print(l)
#     elif x[0] == "remove":
#         l.remove(x[1])
#     elif x[0] == "pop":
#         l.pop()
#     elif x[0] == "reverse":
#         l.reverse()
#     elif x[0] == "sort":
#         l.sort()
#     x = []
# import re
# for i in range(int(input())):
#     ans = True
#     try:
#         x = re.compile(input())
#     except re.error:
#         ans = False
#     print ans

#----------Minion Game--------------
# s = 0
# w = 0
# string  = "BANANANAAAS"
# vowels = ["A","E","I","O","U"]
# for i in range(len(string)):
#     if string[i].upper() in vowels:
#         s += len(string)-i
#     else:
#         w += len(string)-i
# print(s,w)

#-------------Merge the tools---------------
# s = "AABCAAADA"
# k = 3
# l = 0
# j = []
# for i in range(k,len(s)+1,3):
#     j.append("".join(dict.fromkeys(s[l:i])))
#     l=i
# print(j)
#-------------itertools----------------
# import itertools
# s = input() 
# for i in s:
#     k = (list(itertools.groupby()))
#     for i in range(len(k)):
#         print("".join(k[i]))
# import itertools
# s = "1222311"
# for k,x in itertools.groupby(s):
#     print((int(k),len(list(x))),end=" ")

#------------palindrome string------------------
# k = ""
# for i in range(1,6):
#     for j in range(1,i+1):
#         k = k+str(j)
        
#     print(k+k[-2::-1])
#     k = ""

#--------------SETS-------------------
# sum  = 0
# arr = [1,2,3,4,5,6,7,6,4,3,2,5,7]
# x = set(arr)
# l = [int(i) for i in x]
# for i in l:
#     sum += i
# print(f'{sum/len(l):.3f}')

#---------------Counter collections---------------
# from collections import Counter

# n = input()
# x = Counter(map(int,input().split()))
# income = 0
# for i in range(int(input())):
#     size , money = map(int,input().split())
#     print(size,money)
#     if x[size]:
#         income += money
#         x[size] -= 1
# print(income)

#----------No IDEA--------------
# happiness = 0
# x,y = map(int,input().split())
# a = list(map(int,input().split()))
# A = set(map(int,input().split()))
# B = set(map(int,input().split()))
# for i in a:
#     if i in A:
#         happiness += 1
#     if i in B:
#         happiness -= 1
# print(happiness)

#----------Sets------------
# x = input()
# x = set(input().split()) 
# y = input()
# for i in range(int(input())):
#     a = input().split()
#     if a[0] == "intersection_update":
        
#-----------company logo------------

    