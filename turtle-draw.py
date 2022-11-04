print("Reading turtle-draw.txt")

txtFileName = "turtle-draw.txt"

file = open(txtFileName, "r")
line = file.readline()

while line: 
        parts=line.split()
        print(parts)
        if (len (parts) ==3):
            print("3 parts")
    
    
        if (len (parts) == 1):
            print("1 part")

            
        line = file.readline()

