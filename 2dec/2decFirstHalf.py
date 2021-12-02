verticalMovement = 0 
horizontalMovement = 0

def moveSubmarine(direction, movement):
    global verticalMovement
    global horizontalMovement
    if(direction == "forward"):
        verticalMovement+=movement
    elif(direction == "up"):
        horizontalMovement-=movement
    elif(direction == "down"):
        horizontalMovement+=movement
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
    global horizontalMovement
    array = formatArray("2dec/movement.txt")
    for i in array:
        moveSubmarine(i[0],int(i[1]))
    print(verticalMovement*horizontalMovement)

main()