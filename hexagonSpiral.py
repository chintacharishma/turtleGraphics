import turtle
colors = ["red","purple","yellow","tomato","green","crimson"]
hexagon = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    hexagon.pencolor(colors[i%6])
    hexagon.width(i/100+1)
    hexagon.forward(i)
    hexagon.left(59)