import turtle


drawing_board=turtle.Screen()
drawing_board.bgcolor("light pink")
drawing_board.title("Drawing Board")

turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_right():
    turtle_instance.setheading(turtle_instance.heading()-10)
   # turtle_instance.right(10)

def rotate_left():
    turtle_instance.setheading(turtle_instance.heading()+10)
   # turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_penup():
    turtle_instance.penup()

def turtle_pendown():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_right,key="Down")
drawing_board.onkey(fun=rotate_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="h")
drawing_board.onkey(fun=turtle_pendown,key="w")

drawing_board.onkey(fun=turtle_penup,key="q")



turtle.mainloop()