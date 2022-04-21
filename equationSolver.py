


def main():
    solveEquation('x + 1 = 9 - 2')
    return

def solveEquation(stringToSolve):
    inputArray = stringToSolve.split()
    removalArray = []
    for i in range(len(inputArray)):
        if inputArray[i] == '=':
            equalsLocation = i
        if inputArray[i] == 'x':
            xLocation = i
        try:
            inputArray[i] = float(inputArray[i])
        except:
            continue
    for i in range(len(inputArray)):
        if inputArray[i] == '+':
            removalArray.append(i)
        elif inputArray[i] == '-':
            removalArray.append(i)            
            inputArray[i+1] = 0 - inputArray[i+1]
    inputArray.remove("+")
    inputArray.remove("-") 
    print(inputArray)            
    return

def fileReader():

    return

def fileWriter():

    return








main()