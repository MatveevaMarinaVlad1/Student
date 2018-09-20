import turtle
turtle.shape("turtle")

turtle.speed(0)
turtle.begin_fill()
turtle.color("yellow")
turtle.pendown()
turtle.circle(100)
turtle.end_fill()
turtle.color("blue")
turtle.penup()

turtle.begin_fill()
turtle.setpos(40.00,100.00)
turtle.pendown()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.setpos(-40.00,100.00)

turtle.begin_fill()
turtle.pendown()
turtle.circle(20)
turtle.end_fill()
turtle.penup()

turtle.color("black")

turtle.setpos(0.00,90.00)
turtle.pendown()
turtle.width(5)
turtle.right(90)
turtle.forward(30)

turtle.penup()

turtle.setpos(-30.00,40.00)
turtle.pendown()
turtle.width(10)
turtle.color("red")
turtle.circle(30,180)
