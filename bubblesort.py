l = [0,4,6,7,2,1,9]
swap = False
while not swap:
    swap = True
    for i in range(0,len(l)-1):
        if l[i] > l[i+1]:
            swap = False
            l[i],l[i+1] = l[i+1],l[i]

print(l)