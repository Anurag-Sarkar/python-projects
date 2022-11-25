#----------------Q1------------------
# year = int(input())
# print("Leap" if year%4 == 0 else "Not Leap")

#----------------Q2------------------
# def checker(n):
#     state = True
#     for i in range(2,n):
#         if n % i == 0:
#             state = False
#     return state

# n = int(input())
# if n == 1:
#     print("1")
#     print("Speical number")
# elif n == 2:
#     print("1,2")
#     print("Prime Number")
# else:
#     print("Prime" if checker(n) else "Not Prime")
#     for i in range(2,n+1):
#         if checker(i):
#             print(i,end=" ")

#----------------Q3------------------
# n = input()
# sum = 0
# for i in range(len(n)):
#     sum += int(n[i])
# print(sum)

#----------------Q4------------------
# z = ""
# n = input()
# for i in range(len(n)-1,-1,-1):
#     z += n[i]
# if n == z:
#     print("Palindrome",z)
# else:
#     print("Not Palindrome",z)

# #----------------Q5------------------
# def armstrong(n):
#     sum = 0
#     for i in n:
#         sum += int(i)**3
#     return sum

# n = input()
# for i in range(int(n)):
#     if i == armstrong(str(i)):
#         print(i,end=" ")
