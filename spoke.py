import turtle

screen=turtle.Screen()
screen.bgcolor("green")

clock = turtle.Turtle()
clock.shape("square")

clock.speed(0)

hours = 6
minutes = 30 

angle = 8              #12

for i in range(angle):
    # draw the leg
    clock.forward(65)
    clock.right(30)
    clock.write(i)

    # go back to the middle and turn back around
    clock.right(180)
    clock.forward(65)
    clock.right(180)
    clock.write(i+1)

clock.shape("circle")
clock.forward(65)

screen.exitonclick()
