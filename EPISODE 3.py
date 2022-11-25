#-----------------Q1-----------------
#--------------FIBONACCI-------------
# i = 0
# j = 1
# k = 1
# n = int(input())
# if n == 0:
#     print("0")
# elif n == 1:
#     print("0 1")
# else:    
#     print("0",end=" ")
#     while k < n:
#         print(k,end=" ")
#         k = i+j
#         i = j
#         j = k

#-----------------Q2-----------------
#--------------FACTORIAL-------------
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)

#-----------------Q3-----------------
#----------------POWER---------------
# number = int(input())
# power = int(input())
# p = 1
# for i in range(power):
#     p *= number
# print(p)

#-----------------Q4-----------------
#---------------FACTOR---------------
# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end=" ")

#-----------------Q5-----------------
#---------------STRONG---------------
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)    
# n = int(input())
# l = n
# s = 0
# for i in range(3):
#     j = l % 10
#     s += factorial(j)
#     l = l // 10
# print(s,n)
# print("Strong Number" if s == n else "Not Strong Number")


