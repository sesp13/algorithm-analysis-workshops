def getCardMoverWinner(arr):
    arrLength = len(arr)
    counter = 0
    while True:
        isSorted = True
        for i in range(1, arrLength):
            lastElement = arr[i - 1]
            currentElement = arr[i]
            if(currentElement < lastElement):
                isSorted = False
                arr[i] = lastElement
                arr[i - 1] = currentElement
                counter += 1

        if isSorted:
            break
    if(counter == 0):
        print("Empate")
    elif(counter % 2 == 0):
        print("Pedro")
    else:
        print("Susana")


def main():
    finalArr = []
    while True:
        cases = int(input())
        caseArr = []
        if(cases == 0):
            break
        for _ in range(cases):
            caseArr.append(int(input()))
        finalArr.append(caseArr)

    for arr in finalArr:
        getCardMoverWinner(arr)


main()
