import turtle
t = turtle.Turtle()
t.color("red")
for side in range(30):
	t.forward(10 * side)
	t.right(360 / 3)
t.hideturtle()