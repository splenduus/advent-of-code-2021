zeroCount = [0]*12
oneCount = [0]*12

gammaRate=[""] *12
epsilonRate=[""]* 12

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

def calculatemostCommonBit(strings):
    global zeroCount
    global oneCount
    global gammaRate #3258
    global epsilonRate #837

    for binaries in strings:
        for index in range(0,len(binaries)):
            if(binaries[index] == "1"): 
                oneCount[index] += 1
            elif(binaries[index] == "0"): 
                zeroCount[index] +=1

    for index in range(0,len(zeroCount)):
        if(zeroCount[index]<oneCount[index]):
            gammaRate[index] = "1"
            epsilonRate[index] = "0"
        else: 
            epsilonRate[index] = "1"
            gammaRate[index]= "0"

def calculatePowerConsumption(gammaRate,epsilonRate):
    powerConsumption = int(''.join(gammaRate),2) * int(''.join(epsilonRate),2)
    print(powerConsumption)

        
def main():
    calculatemostCommonBit(readFile("3dec/binary.txt"))
    calculatePowerConsumption(gammaRate,epsilonRate)

main()