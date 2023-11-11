import turtle

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Langton's Ant")

tileMap = {}

ant = turtle.Turtle("square")
ant.resizemode("user")
ant.shapesize(.95, .95)
ant.speed(0)

for i in range (0, 1000):
    pos = str(ant.pos())
    tile = tileMap.get(str(pos))
    if pos not in tileMap or tile == "white":
        ant.color("black")
        ant.stamp()
        ant.left(90)
        ant.forward(20)
        tileMap[pos] = "black"
    else:
        ant.color("white")
        ant.stamp()
        ant.right(90)
        ant.forward(20)
        tileMap[pos] = "white"

screen.exitonclick()


