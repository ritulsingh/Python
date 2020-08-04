import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
t.speed(10)
c=0

while True:
    for i in range(4):
        t.forward(180)
        t.right(90)
    t.right(5)
    c +=1
    if c>= 360/5:
        break
t.hideturtle()
turtle.done()