#alice or bob
def floor(n):
    if n%10 == 0:
        return n//10
    else:
        return (n//10)+1
chance = "alice"
for i in range(int(input())):
    p1,p2 = map(int,input().split())
    print(abs(floor(p1)-floor(p2)))