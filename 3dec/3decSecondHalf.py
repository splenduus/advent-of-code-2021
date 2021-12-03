zeroCount = [0]*12
oneCount = [0]*12

strings =""

def readFile(fileName):
    global strings 
    fileObj = open(fileName, "r") #opens the file in read mode
    strings = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()


def calculatemostCommonBit(string):
    global zeroCount
    global oneCount

    zeroCount = [0] *12
    oneCount = [0] *12

    for binaries in string:
        for index in range(0,len(binaries)):
            if(binaries[index] == "1"): 
                oneCount[index] += 1
            elif(binaries[index] == "0"): 
                zeroCount[index] +=1

def calculateOxygen():
    global zeroCount
    global oneCount
    global strings
    copyString = strings.copy()

    for index in range(0,12):
        string2 = copyString.copy()
        calculatemostCommonBit(string2)
        if(len(copyString) > 1):
            for binaries in string2:
                if(len(copyString)>1):
                    if(oneCount[index]>=zeroCount[index] and binaries[index] == "0"):
                            copyString.remove(binaries)
                    elif(oneCount[index]<zeroCount[index] and binaries[index] == "1"):
                            copyString.remove(binaries)
                else : break
        else: 
            break
    return copyString

def co2scrubber():
    global zeroCount
    global oneCount
    global strings
    copyString = strings.copy()

    for index in range(0,12):
        string2 = copyString.copy()
        calculatemostCommonBit(string2)
        if(len(copyString) > 1):
            for binaries in string2:
                if(len(copyString)>1):
                    if(oneCount[index]>=zeroCount[index] and binaries[index] == "1"):
                            copyString.remove(binaries)
                    elif(oneCount[index]<zeroCount[index] and binaries[index] == "0"):
                            copyString.remove(binaries)
                else : break
        else: break
    return copyString
        
def calculateEnergy():
    oxygen= calculateOxygen()
    co2 = co2scrubber()
    print(int(''.join(oxygen),2)*int(''.join(co2),2))

def main():
    readFile("3dec/binary.txt")
    calculatemostCommonBit(strings)
    calculateEnergy()

main()