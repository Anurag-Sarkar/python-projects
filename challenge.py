

# entry = [2,5,1,3]
# exit = [0,6,2,1]
# guest = 0
# x = []
# maxi = 0
# for i in range(len(entry)):
#     guest = guest - (entry[i] - exit[i])
#     x.append(abs(guest)) 
# for i in x:
#     if i > maxi:
#         maxi = i
# print(maxi)



# n = 10
# k = 5
# i = int(input())
# while n >= k:
#     if i == 0 or i > k:
#         print("INVALID INPUT") 
#         print("NUMBER OF CANDIES AVAILABLE: ",n) 
#         break
#     else:
#         n = n - i 

#         if n > 5:
#             print("NUMBER OF CANDIES SOLD: ",i)
#             print("NUMBER OF CANDIES LEFT: ",n) 



# s = input()
# star = 0
# hash = 0

# for i in s:
#     if i == "*":
#         star += 1
#     if i == "#":
#         hash += 1

# if hash > star:
#     print(star-hash)
# elif star > hash:
#     print(star-hash)
# elif hash == star:
#     print(0)