# Draw triangles of triangles
from turtle import *


# Draw a triangle
for sides in range(1, 4):
    forward(40)
    left(120)

# Move to position for second triangle
penup()
forward(100)
pendown()

# Draw a triangle
for sides in range(1, 4):
    forward(40)
    left(120)

# Move to position for third triangle
penup()
left(180)
forward(100)
right(90)
forward(100)
right(90)
pendown()

# Draw a triangle

for sides in range(1, 4):
        forward(40)
        left(120)


