import turtle
import math
r=20
n=3
turtle.speed(0)
for i in range(0,7):
    turtle.pendown()
    turtle.circle(-r)
    alpha=360/n
    storona=2*r*math.sin(math.pi/n)
    k=0.00
    m=0.00
    for j in range(1,n+1):
        turtle.setheading(-(alpha*j-alpha/2))
        turtle.forward(storona)
        turtle.setheading(-alpha*j)
    turtle.penup()
    turtle.setpos(k, m+r)
    r=r+20
    n=n+1
    
'''import turtle
import math
turtle.shape("turtle")
def shape(rad,nun):
    angle=360/n
    angler=angle*3.14/180
    a=rad*(2*math.sin(angler))
    return a
r=20
k=0
m=0
for j in range(1,8):
    turtle.setpos(k,m)
    turtle.pendown()
    turtle.circle(r)

    turtle.penup()

    n=3

    rol=shape(r,n)
    angle=360/n
    turtle.setpos(0,0)

    for i in range(1,n+1):
        turtle.pendown()
        turtle.setheading(angle*i)
        turtle.forward(rol)
    n=n+1
    r=r+20
    m=m-20'''

