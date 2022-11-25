arr1 = [1,2,3,[4,5]]
arr2 = [1,2,[3,4]]
res = []
for i in range(len(arr2)):
    if type(arr1[i]) == int and type(arr2[i]) == int:
       res.append(arr1[i]+arr2[i]) 
    elif type(arr1[i]) == list and type(arr2[i]) == int:
        

print(res)