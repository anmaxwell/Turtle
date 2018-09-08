def drawing_M():

	backclr = input("Choose your background colour")
	penclr = input("Choose your pen colour")

	import turtle

	wn = turtle.Screen()
	wn.bgcolor(backclr)        # set the window background 

	tess = turtle.Turtle()
	tess.color(penclr)              # set the pen colour
	tess.pensize(5)                 # set the width of the pen

	tess.left(90)
	tess.forward(150)
	tess.right(135)
	tess.forward(50)
	tess.left(90)
	tess.forward(50)
	tess.right(135)
	tess.forward(150)

	wn.exitonclick()                # wait for a user click on the canvas


if __name__ == "__main__":
    drawing_M()