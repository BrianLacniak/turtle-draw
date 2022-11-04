# TurtleDraw
# Brian Lacniak
# Lewis University 2022 

import turtle

print("Reading turtle-draw.txt")

turtleScreen = turtle.Screen()
turtleScreen.setup(450,450)

turtleApp = turtle.Turtle()

txtFileName = "turtle-draw.txt"

file = open(txtFileName, "r")
line = file.readline()

while line: 
        parts=line.split()
        print(parts)
        if (len (parts) ==3):
            print(parts[0])
            print(int(parts[1]))
            print(int(parts[2]))
    
    
        if (len (parts) == 1):
            print("1 part")


        line = file.readline()

