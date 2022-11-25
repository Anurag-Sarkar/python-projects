#-----------------Q1----------------
#-----------------HCF---------------
# def hcf(n,m):
#     x = 0
#     i = (n if n>m else m)
#     for i in range(1,i+1):
#         if n % i == 0 and m % i == 0:
#             x = i        
#     return x
# print(hcf(12,18))


#-----------------Q1----------------
#-----------------LCM---------------     
# n = int(input())
# m = int(input())
# x = 0
# y = 1
# i = 2
# while x != y:
#     if i % n == 0 or n % i == 0:
#         x = i
#     if i % m == 0 or m % i == 0:
#         y = i
#     i += 1
    
# print("LCM is",x)

#-----------------Q3----------------
#-----------------GCD---------------     
# def divisor(n+1):
#     l = []
#     for i in range(1,n):
#         if n % i == 0:
#             l.append(i)
#     return l

# n = int(input())
# m = int(input())
# x = set(divisor(n))
# y = set(divisor(m))
# print(max(set.intersection(x,y)))

#-----------------Q4----------------
#--------------QUADRANT-------------     
# x,y = map(int,input("X : Y Values: ").split())
# if x > 0 and y > 0:
#     print("1st Quadrant")
# elif x > 0 and y < 0:
#     print("3rd Quadrant")
# elif x < 0 and y > 0:
#     print("2nd Quadrant")
# elif x < 0 and y < 0:
#     print("4th Quadrant")

#-----------------Q5----------------
#-------------PERMUTATION-----------     
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# n = int(input())
# r = int(input())

# print(factorial(n)//factorial(n-r))

#----------------Q6-----------     
#-------------HANDSHAKES-----------     
# n = int(input())
# h = 0
# for i in range(1,n):
#     h += i
# print("No of handshakes are",h)

 

#----------------Q8----------------     
#--------REPLACING 1 WITH 0--------   
# i = [i for i in input()]
# for k,v in enumerate(i):
#     if v == "0":
#         i.pop(k)
#         i.insert(k,"1")
# print("".join(i))

#----------------Q9----------------     
#--------TWO PRIME NUMBER----------
# def prime(n):
#     state = True
#     for i in range(2,n):
#         if n%i == 0:
#             state = False
#             break
#     return state
# n = int(input())
# l = []
# for i in range(n):
#     if prime(i):
#         l.append(i)

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i] + l[j] == n:
#             print(l[i],l[j])

# ----------------Q10----------------     
# --------VOWEL OR CONSONANTS--------   
# c = input()
# v = ["a","e","i","o","u"]
# if c.lower() in v:
#     print("Vowel")
# else:
#     print("Consonants")

#12
def traingle_numbers(r):
    sum = 0
    for i in range(r):
        sum += i
    return sum

for i in range(1,9):
    print(traingle_numbers(i))























