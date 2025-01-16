import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python turtle")

turtle_instance=turtle.Turtle()
turtle_instance.color("red")
turtle.speed(0)
turtle_colors=["red","orange","purple","blue","yellow","green"]


for i in range(20):
    turtle_instance.color(turtle_colors[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)

#turtle.done()

#turtle.mainloop()