import turtle
s = turtle.getscreen()
t = turtle.Turtle()

for i in range(4):
    n = 10
    while n <= 40:
        t.circle(n)
        n = n + 10
    t.rt(90)