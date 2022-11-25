import math

def if_root(a,b,c):
    if ((b*b)-(4*a*c)) == 0:
        x = math.floor((-b + math.sqrt(((b*b)-(4*a*c))))/2)
        y = math.floor((-b - math.sqrt(((b*b)-(4*a*c))))/2)
        return x,y

    if ((b*b)-(4*a*c)) > 0:
        x = math.floor((-b + math.sqrt(((b*b)-(4*a*c))))/2)
        y = math.floor((-b - math.sqrt(((b*b)-(4*a*c))))/2)
        return x,y

    else:
        return "No real Roots"

a = input("Enter value of x^2")
b = input("Enter value of x")
c = input("Enter value of constant")
print(if_root(a,b,c))