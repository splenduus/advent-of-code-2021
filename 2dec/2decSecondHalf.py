verticalMovement = 0 
depth = 0
aim = 0

def moveSubmarine(direction, movement):
    global verticalMovement
    global depth
    global aim
    if(direction == "forward"):
        verticalMovement +=  movement
        if(aim != 0):
            depth += movement * aim
    elif(direction == "up"):
        aim -= movement
    elif(direction == "down"):
        aim += movement
    return 

def formatArray(file):
    file_input = open(file,"r")
    words = file_input.read().splitlines()
    tupleArray = []
    for i in words:
        tupleArray.append(i.split(" "))
    return tupleArray

def main():
    global verticalMovement
    global depth
    array = formatArray("2dec/movement.txt")
    for i in array:
        moveSubmarine(i[0],int(i[1]))
    print(verticalMovement*depth)

main()