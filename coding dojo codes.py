from array import array
from platform import java_ver
import random
import string
#------------name sorter--------------
# def loop(k,l):
#   if(k>0):
#     r = 1+loop(k-1,l)
#     if l[r][0] == "S" or l[r][0]=="s":
#         print(l[r],end=" ")
#   else:
#     r = -1
#   return r

# l = ("Samarth","Ankush","Sourav","Sanket","Kajal")
# loop(len(l),l)

#-----------matrix input--------------
# a = []
# for i in range(4):
#     q = []
#     for i in range(2):
#         q.append(input())
#     a.append(q)
# print(a)

#----------2 matrix sum--------------
# l = [[1,2],[3,4]]
# m = [[5,6],[7,8]]
# o = []
# for i in range(2):
#     r = []
#     for j in range(2):
#         r.append(l[i][j]+m[i][j])   
#     o.append(r)
# print(o)

#-----------matrix sum-------------
# a = 0
# l = [[1,2],[3,4]]
# for i in l:
#     for j in i:
#         a = a + j
# print(a)

#--------------Diagonal sum--------------
# result = 0
# z = [[1,2,3],[2,3,4],[8,9,0]]
# for i in range(len(z)):
#   for j,v in enumerate(z[i]):
#     if i==j:
#       result = result + z[i][j]
# print(result)
#--------Opposite diagonal----------
# result = 0
# z = [[6,2,3],[4,8,9],[2,4,6]]
# for i in range(len(z)):
#   print(i,(len(z[i])-1-i))
#   result += z[i][len(z[i])-1-i] 
# print(result)

#----------------Reversing list----------------
# arr = array("i",[3,5,2,4,6])
# for i in range(len(arr)):
#   l = arr.pop()
#   arr.insert(i,l)
# print(arr)

#-------------multi point reverse listSsss-------------
# arr = array("i",[1,2,3,4,5,6,7,8])
# start = 0
# end = len(arr)-1
# while start<=end:
#   arr[start],arr[end] = arr[end],arr[start]
#   start += 1
#   end -= 1
# print(arr)
 
 #--------------upper trainglr matrix----------------
# sum = 0
# z = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# for i in range(len(z)):
#   for j in range(len(z)-i):
#     sum += z[i][j+i]
# print(sum)

# ----------LOWER traingle matrix------------
# sum = 0
# z = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(z)):
#   for j in range(0,i+1):
#     sum += z[i][j]
# print(sum)

#-----------travesing list-----------------
# sum = 0
# z = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(len(z)):
#   for j in range(0,i):
#     z[i][j],z[j][i]=z[j][i],z[i][j]
# print(z)

#-------------traversing non square matrix----------------
# q = []
# z = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# for i in range(len(z[0])):
#   m = []
#   for j in range(len(z)):
#     m.append(z[j][i])
#   q.append(m)
# print(q)

# z = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(len(z)):
#   for j in range(len(z)):
#     if i != len(z)-1 or j != len(z)-1:
#       z[i][j]

#----------------Rotating a matrix-----------------
# l = []
# k = []
# z = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(z)):
#     for j in range(len(z)):
#         l.append(z[i][j])
# for i in range(len(l)-1):
#     l[i],l[i+1] = l[i+1],l[i]
# for i in range(len(z)):
#     m = []
#     for j in range(len(z)):
#         m.append(l)
#     k.append(m)
# print(k)

#--------------OOPS calc-----------------
# class Calc:
#     def __init__(self,a,b):
#         self.__a = a
#         self.__b = b
#     def sub(self):
#         return abs(self.__a - self.__b)
    
#     def sum(self):
#         return self.__a + self.__b

# a,c,b = input().split()
# calc = Calc(int(a),int(b))
# if c == "+":
#     print(calc.sum())
# elif c == "-":
#     print(calc.sub())

#--------------OOP Products-----------
# try:
#     class Product:
#         __productCount = 0

#         def __init__(self):
#             self.__products = {}

#         def Create(self , id: int , name:str , cost:int):
#             Product.__productCount += 1
#             if id in self.__products.keys():
#                 print("!!! ID Already exists, Enter a Unique ID")
#             else:
#                 self.__products[id] = {"ID" : id,"NAME" : name,"PRICE" : cost}
#                 print("-> Entered Successfully")

#         def ShowAll(self):
#             return self.__products
        
#         def Delete(self,id:int):
#             del self.__products[id]

#         def ShowOne(self,id):
#             return (self.__products.get(id))

#         def Update(self,id):
#             key = input("Enter Key: ")
#             value = input("Enter Value: ")
#             if key in self.__products[id].keys():
#                 self.__products[id][key] = value
#                 print("-> Updates Successfully")
#             else:
#                 print("!!! Key Isn't Found")

#         @classmethod 
#         def TotalCount(cls):
#             return cls.__productCount
            

#     prod = Product()
#     prod.Create(1,"Fridge",10000)
#     prod.Create(2,"Mobile",20000)
#     prod.Create(3,"Television",300000)
#     e = 1
#     print(Product.TotalCount())
#     while e != 0:
#         print("\n1: TO CREATE PRODUCT") 
#         print("2: TO UPDATE PRODUCT") 
#         print("3: TO DELETE PRODUCT") 
#         print("4: TO SHOW PRODUCT") 
#         print("5: TO SHOW ALL PRODUCT") 
#         print("6: TO SHOW TOTAL PRODUCTS") 
#         print("7: TO EXIT\n")
#         x = int(input())
#         if x == 1:
#             id,name,cost = input("Enter ID, Name, Cost: ").split()
#             prod.Create(int(id),name,int(cost))
#         if x == 2:
#             prod.Update(int(input("Enter ID: ")))
#         if x == 3:
#             prod.Delete(int(input("Enter ID: ")))
#             print("-> Deleted Successfully")
#         if x == 4:
#             print(prod.ShowOne(int(input("Enter ID: "))))
#         if x == 5:
#             k = prod.ShowAll()
#             for key in k:
#                 print(k[key])
#         if x == 6:
#             print("Total Products: ",Product.TotalCount())
#         if x == 7:
#             e = 0
# except ValueError:
#     print("!!! Error - Enter Details Properly")
# except KeyError:
#     print("!!! Error - Specified ID Not Found")


#-------------OOPS MAGIC METHODS----------------
# class Add:
#     def __init__(self,n):
#         self.__n = n
    
#     def __str__(self):
#         return self.__n


#     def __add__(self,other):
#         return self.__n + other.__n
    
#     def __sub__(self,other):
#         return self.__n - other.__n

#     def __mul__(self,other):
#         return self.__n * other.__n

#     def __mod__(self,other):
#         return self.__n % other.__n
    
#     def __truediv__(self,other):
#         return self.__n / other.__n

    
# print("Enter two numbers: ")
# obj1 = Add(int(input("Number 1: ")))
# obj2 = Add(int(input("Number 2: ")))
# op = input("Enter Operator: ")

# if op == "+":
#     print(obj1 + obj2)
# if op == "-":
#     print(obj1 - obj2)
# if op == "*":
#     print(obj1 * obj2)
# if op == "%":
#     print(obj1 % obj2)
# if op == "/":
#     print(obj1 / obj2)

#----------------Guess game---------------
# x = random.randint(1,100)
# print(x)

# for i in range(5):  
#   y = int(input("Guess the number: "))
#   if x < y:
#     print("Too High")
  
#   if x > y:
#     print("Too Low")
  
#   if x == y:
#     print("Yaa..! you guessed the number")
#     break

# else:
#   print("You Lost The Number Was: ",x)

#---------------random password generator---------------
# def Generator(len):
#   x = (string.digits + string.ascii_letters + string.punctuation)
#   y = random.choices(x , k=len)
#   return y

# i,j = map(int,input("Enter no of password and length").split())

# for i in range(i):
#   print("".join(Generator(j)))

string = "john doe"
hash = {}
for i in string:
  hash[i] = hash[i]+1 if i in hash else 1
print(hash)

print("Duplicate" if i in hash.values() else "no Duplicate" for i in hash)