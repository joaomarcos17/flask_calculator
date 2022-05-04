# create triangles
from turtle import *

# set up gloves variable
gloves = [10,8,2,5]

# produce x axis
goto(120,0)

# produce y axis
goto(0,0)
goto(0,150)

# plot data
goto(0,0)

for index in range(len(gloves)):
    goto((20 * index), gloves[index] * 10)
