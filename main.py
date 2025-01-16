import turtle


drawing_board=turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Python turtle")


#star
'''
turtle_instance=turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(200)
'''


#polygon

turtle_instance=turtle.Turtle()
num_side=5
angle=360/num_side*2
side_length=100

for i in range(num_side):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)    

    


turtle.done()