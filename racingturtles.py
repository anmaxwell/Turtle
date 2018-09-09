def racing():

	import turtle              # 1.  import the modules
	import random
	track = turtle.Screen()       # 2.  Create a screen
	track.bgcolor('lightblue')

	lance = turtle.Turtle()    # 3.  Create two turtles
	andy = turtle.Turtle()
	lance.color('red')
	andy.color('blue')
	lance.shape('turtle')
	andy.shape('turtle')

	andy.up()                  # 4.  Move the turtles to their starting point
	lance.up()
	andy.goto(-100,20)
	lance.goto(-100,-20)

	a = andy.pos()
	l = lance.pos()

	while a[0] <50 or l[0] <50:
		andymove = random.randrange(1,10)
		lancemove = random.randrange(1,10)
    
		andy.forward(andymove)
		lance.forward(lancemove)
    
		a = andy.pos()
		l = lance.pos()

	if a[0] > l[0]:
		winner = andy
		andy.write("andy wins   ", align="right")
	else:
		winner = lance
		lance.write("lance wins   ", align="right")

	for spin in range(24):
		winner.right(90)


	track.exitonclick()

if __name__ == "__main__":
    racing()


