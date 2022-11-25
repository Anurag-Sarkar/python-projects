import math
from turtle import right
#3
# def primeFactors(n):
 
#     c = 2
#     while(n > 1):
 
#         if(n % c == 0):
#             print(c, end=" ")
#             n = n / c
#         else:
#             c = c + 1

# n = 10001
# primeFactors(n)
 
#4
# n = []
# for i in range(100,1000):
#     for j in range(100,1000):
#         x = str(i*j)
#         if x == x[::-1]:
#             n.append(i*j)
# print(max(n))       

#5
# n = 21
# while True:
#     if n%1 == 0 and n%2 == 0 and n%3 == 0 and n%4 == 0 and n%5 == 0 and n%6 == 0 and n%7 == 0 and n%8 == 0 and n%9 == 0 and n%10 == 0 and n%11 == 0 and n%12 == 0 and n%13 == 0 and n%14 == 0 and n%15 == 0 and n%16 == 0 and n%17 == 0 and n%18 == 0 and n%19 == 0 and n%20 == 0:
#         print(n)
#         break
#     else:
#         n+=1    

#6
# sq = lambda x : x**2
# sq_sum = 0
# sum_sq = 0
# for i in range(1,101):
#     sum_sq += i
#     sq_sum += sq(i)
# print(sq_sum)
# print(sum_sq**2)
# print(sum_sq**2-sq_sum)

#7
# def check_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         return n
# n = 2
# prime_count = 0
# while True:
#     if prime_count == 10001:
#         print(x)
#         break
#     x = check_prime(n)
#     if x:
#         prime_count+=1
#     n+=1

#8
# def multi(n):
#     multiply = 1
#     for i in n:
#         multiply *= int(i)
#     return multiply
# str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# m = []
# for i in range(988):

#     x = multi(str[i:i+13])
#     if x != 0:
#         m.append(x)
# print(max(m))
    
#9
# print("printing...")
# for m in range(1,50):
#     for n in range(1,m):
#         a = m * m - n * n
#         b = 2 * m * n
#         c = m * m + n * n
#         # print(a,b,c)
#         # print(a,b,c)
#         if a+b+c == 1000:
#             print(a*b*c)

#10 not efficient
# def check_prime(n):
#     for i in range(2):
#         if n % i == 0:
#             break
#     else:
#         return n
# n = 2
# suum = 0
# prime_count = 0
# for i in range(2,10):
#     x = check_prime(n)
#     if x:
#         print(x)
#         suum += x
#     n+=1
# print(suum)

#11
# def left_diagonal_product(grid):
#     product = 1
#     for i in range(4):
#         product *= grid[i][i]
#     return product

# def right_diagonal_product(grid):
    
#     product = 1
#     for i in range(4):
#         product *= grid[i][3-i]

#     return product

# def horizintal_product(grid):
#     product = []
#     for i in range(4):
#         x = 1
#         for j in range(4):
#             x *= grid[i][j]
#         product.append(x)
#     return product

# def verticle_product(grid):
#     product = []
#     for i in range(4):
#         x = 1
#         for j in range(4):
#             x *= grid[j][i]
#         product.append(x)
#     return product

# def grid_chooser(grid,k,l):
    
#     sgrid = []
#     for i in range(k,k+4):
#         x = []
#         for j in range(l,l+4):
#             x.append(grid[i][j])
#         sgrid.append(x)
#     return sgrid

# grid =[[8 ,2 ,22 ,97 ,38 ,15 ,00 ,40 ,00 ,75 ,4 ,5 ,7 ,78 ,52 ,12 ,50 ,77 ,91 ,8],
#        [49 ,49 ,99 ,40 ,17 ,81 ,18 ,57 ,60 ,87 ,17 ,40 ,98 ,43 ,69 ,48 ,4 ,56 ,62 ,00],
#        [81 ,49 ,31 ,73 ,55 ,79 ,14 ,29 ,93 ,71 ,40 ,67 ,53 ,88 ,30 ,3 ,49 ,13 ,36 ,65],
#        [52 ,70 ,95 ,23 ,4 ,60 ,11 ,42 ,69 ,24 ,68 ,56 ,1 ,32 ,56 ,71 ,37 ,2 ,36 ,91],
#        [22 ,31 ,16 ,71 ,51 ,67 ,63 ,89 ,41 ,92 ,36 ,54 ,22 ,40 ,40 ,28 ,66 ,33 ,13 ,80],
#        [24 ,47 ,32 ,60 ,99 ,3 ,45 ,2 ,44 ,75 ,33 ,53 ,78 ,36 ,84 ,20 ,35 ,17 ,12 ,50],
#        [32 ,98 ,81 ,28 ,64 ,23 ,67 ,10 ,26 ,38 ,40 ,67 ,59 ,54 ,70 ,66 ,18 ,38 ,64 ,70],
#        [67 ,26 ,20 ,68 ,2 ,62 ,12 ,20 ,95 ,63 ,94 ,39 ,63 ,8 ,40 ,91 ,66 ,49 ,94 ,21],
#        [24 ,55 ,58 ,5 ,66 ,73 ,99 ,26 ,97 ,17 ,78 ,78 ,96 ,83 ,14 ,88 ,34 ,89 ,63 ,72],
#        [21 ,36 ,23 ,9 ,75 ,00 ,76 ,44 ,20 ,45 ,35 ,14 ,00 ,61 ,33 ,97 ,34 ,31 ,33 ,95],
#        [78 ,17 ,53 ,28 ,22 ,75 ,31 ,67 ,15 ,94 ,3 ,80 ,4 ,62 ,16 ,14 ,9 ,53 ,56 ,92],
#        [16 ,39 ,5 ,42 ,96 ,35 ,31 ,47 ,55 ,58 ,88 ,24 ,00 ,17 ,54 ,24 ,36 ,29 ,85 ,57],
#        [86 ,56 ,00 ,48 ,35 ,71 ,89 ,7 ,5 ,44 ,44 ,37 ,44 ,60 ,21 ,58 ,51 ,54 ,17 ,58],
#        [19 ,80 ,81 ,68 ,5 ,94 ,47 ,69 ,28 ,73 ,92 ,13 ,86 ,52 ,17 ,77 ,4 ,89 ,55 ,40],
#        [4 ,52 ,8 ,83 ,97 ,35 ,99 ,16 ,7 ,97 ,57 ,32 ,16 ,26 ,26 ,79 ,33 ,27 ,98 ,66],
#        [88 ,36 ,68 ,87 ,57 ,62 ,20 ,72 ,3 ,46 ,33 ,67 ,46 ,55 ,12 ,32 ,63 ,93 ,53 ,69],
#        [4 ,42 ,16 ,73 ,38 ,25 ,39 ,11 ,24 ,94 ,72 ,18 ,8 ,46 ,29 ,32 ,40 ,62 ,76 ,36],
#        [20 ,69 ,36 ,41 ,72 ,30 ,23 ,88 ,34 ,62 ,99 ,69 ,82 ,67 ,59 ,85 ,74 ,4 ,36 ,16],
#        [20 ,73 ,35 ,29 ,78 ,31 ,90 ,1 ,74 ,31 ,49 ,71 ,48 ,86 ,81 ,16 ,23 ,57 ,5 ,54],
#        [1 ,70 ,54 ,71 ,83 ,51 ,54 ,69 ,16 ,92 ,33 ,48 ,61 ,43 ,52 ,1 ,89 ,19 ,67 ,48]]


# sgrid = []

# product = []
# for i in range(17):
#     for j in range(17):
#         sgrid.append(grid_chooser(grid,i,j))
# print(len(sgrid))
# for i in sgrid:
#     # print(i)
#     product.append(left_diagonal_product(i))
#     product.append(right_diagonal_product(i))
#     k = horizintal_product(i)
#     for l in k:
#         product.append(l)
#     c = verticle_product(i)
#     for m in c:
#         product.append(m)

# print(max(product))

#12
# def traingle_numbers(r):
#     sum = 0
#     for i in range(r):
#         sum += i
#     return sum

# def divisor(n):
#     div = []
#     for i in range(1,n):
#         if n%i == 0:
#             div.append(i)
#     return div

# i = 1
# while True:
#     k = traingle_numbers(i)
#     if len(divisor(k)) >= 500:
#         print(k)
#     i += 9

#14
# def chain(i):
#     a = []
#     while i != 1:
#         if i%2 == 0:
#             i = i//2
#         elif i%2 == 1:
#             i = (3*i) + 1
#         a.append(i)
#     return a
# j = []
# for k in range(1,1000000):
#     j.append(len(chain(k)))
#     if len(chain(k)) == 524:
#         print(k)
#         break

# print(max(j))

#16
# x = str(2**1000)
# sum = 0
# for i in x:
#     sum += int(i)
# print(sum)

#17
# sum = 0
# with open("lol.txt","r") as f:
#     x = f.readlines()
#     for i in x:
#         sum += (len(i)-1)
# print(sum)
            
#18
# grid = [
#                           [75],
#                         [95 ,64],
#                       [17 ,47 ,82],
#                     [18 ,35 ,87 ,10],
#                    [20 ,4 ,82 ,47 ,65],
#                  [19 ,1 ,23 ,75 ,3 ,34],
#                [88 ,2 ,77 ,73 ,7 ,63, 67],
#              [99 ,65 ,4 ,28 ,6 ,16, 70 ,92],
#           [41 ,41 ,26 ,56 ,83 ,40, 80 ,70 ,33],
#         [41 ,48 ,72 ,33 ,47 ,32, 37 ,16 ,94 ,29],
#       [53 ,71 ,44 ,65 ,25 ,43, 91 ,52 ,97 ,51 ,14],
#     [70 ,11 ,33 ,28 ,77 ,73, 17 ,78 ,39 ,68 ,17, 57],
#   [91 ,71 ,52 ,38 ,17 ,14, 91 ,43 ,58 ,50 ,27, 29 ,48],
#  [63 ,66 ,4 ,68 ,89 ,53, 67 ,30 ,73 ,16 ,69, 87 ,40, 31],
# [4 ,62 ,98 ,27 ,23, 9, 70 ,98 ,73 ,93 ,38, 53 ,60, 4, 23]
# ]
# sum = grid[0][0]
# print(sum)
# index = 0
# for i in range(1,len(grid)):
#     check = []
#     if index == 0:
#         check.append(grid[i][index])
#         check.append(grid[i][index+1])
#     if index > 0:
#         check.append(grid[i][index-1])
#         check.append(grid[i][index])
#         check.append(grid[i][index+1])
#     sum += max(check)
#     x = max(check)
#     print(check)
#     print(x)
#     index = grid[i].index(x)
# print(sum)

#20
# def factorial(n):
#     if n > 1:
#         return factorial(n-1)*n
#     else:
#         return 1

# x = str(factorial(100))
# sum = 0
# for i in x:
#     sum += int(i)

# print(sum)

#21
# def divisors(n):
#     sum = 0
#     for i in range(1,n):
#         if n%i == 0:
#             sum += i
#     return sum 
# sum = 0
# for i in range(1,10000):
#     x = divisors(i)
#     y = divisors(x)
#     if i == y:
#         print(x,y)
#         sum += i
# print(sum)

#22
with open("p022_names.txt" ,"r") as f:
    z = f.readlines()

print(sorted(z))
