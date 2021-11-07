def getMaxBeverages(capArr):
    beverages = 0
    capArr = sorted(capArr)
    while True:
        biggestCapIndex = len(capArr) - 1
        biggestCap = capArr[biggestCapIndex]
        combinationFound = False
        newArr = []
        for i in range(biggestCapIndex):
            currentCap = capArr[i]
            if(biggestCap + currentCap >= 1000):
                # Build next array
                newArr = capArr
                # Remove current item
                newArr.pop(i)
                # Remove last item
                newArr.pop()
                # Increment beverages count
                beverages += 1
                combinationFound = True
                break

        if (combinationFound):
            # If the new arr is empty break
            if(len(newArr) == 0):
                break
            # Set array for the next cycle
            capArr = newArr
        else:
            # If there are not any combinations end the cycle
            break

    print(beverages)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        numberOfCaps = int(input())
        capArr = []
        for __ in range(numberOfCaps):
            capArr.append(int(input()))
        finalArr.append(capArr)

    for capArr in finalArr:
        getMaxBeverages(capArr)


main()
