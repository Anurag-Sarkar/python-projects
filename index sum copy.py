n = [1,2,3,4,5]

def indexing(x):
    a = 0
    b = 0
    for i in range(x+1,len(n)):
        if n[x] + n[i] == target:
            a = x
            b = i
            print(a,b)
    return(a,b)



# n = list(map(int,input("Enter values: ").split(" ")))
# target = int(input('target: '))
target = 9
for i in range(len(n)):
    x = indexing(i)
print(x)