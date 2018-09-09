def stamps():

	import turtle

	wn = turtle.Screen()
	wn.bgcolor("green")        # set the window background

	adam = turtle.Turtle()
	adam.shape("turtle")
	adam.color("blue")

	adam.penup() # picks the pen up

	for size in range(3):
		adam.forward(50)
		adam.stamp()


	wn.exitonclick()
    
if __name__ == "__main__":
    stamps()
