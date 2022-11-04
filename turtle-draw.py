# TurtleDraw
# Brian Lacniak
# Lewis University 2022 

import turtle

print("Reading turtle-draw.txt")

turtleScreen = turtle.Screen()
turtleScreen.setup(450,450)

turtleApp = turtle.Turtle()

turtleApp.color("green")
turtleApp.goto(100,100)


txtFileName = "turtle-draw.txt"

file = open(txtFileName, "r")
line = file.readline()

while line: 
        parts=line.split(" ")
        print(parts)
        if (len (parts) ==3):
            color = parts[0]
            x = int(parts[1])
            y = int(parts[2])
            turtleApp.color(color)
            turtleApp.goto(x, y)
            turtleApp.pendown()
    
        if (len (parts) == 1):
            turtleApp.penup()

           


        line = file.readline()

turtle.done()
