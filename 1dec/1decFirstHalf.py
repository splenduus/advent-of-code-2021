def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    numbers = [int(numeric_string) for numeric_string in words]
    fileObj.close()
    return numbers

def checkDepth(depths):
    counter = 0
    for i in range(0,len(depths)-1):
        if(depths[i] < depths[i+1]):
            counter +=1
    return counter

def main():
    depthsArray = readFile("1dec/depths.txt")
    print(checkDepth(depthsArray))

main()