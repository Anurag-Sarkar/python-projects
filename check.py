def check(l):
    k = []
    state = True
    for i in range(len(l)):
        print(l[i])
        if len(l[i]) != len(l):
            state = False
        return state

j = [[1,2],[3,4,5]]
check(j)
print("EQUAL" if check(j) else "NOT EQUAL")