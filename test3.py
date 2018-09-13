print("enter a, b, c")
a = int(input())
b = int(input())
c = int(input())

d = b*b-4*a*c
print("D = ", d)
if d<0:
    print("no!")
if d>0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
if d==0:
    x1=-b/(2*a)
    print("x1 = ", x1)

print("end")
