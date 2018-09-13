import turtle
turtle.shape("turtle")
x=10
k=0
for i in range(1,10):
    turtle.setpos(k,k)
    turtle.pendown()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    x=x+10
    k=k-5
    turtle.penup()
   


