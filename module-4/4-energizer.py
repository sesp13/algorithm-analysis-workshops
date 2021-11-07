def getMaxBeverages(capArr):
    beverages = 0

    capArr = sorted(capArr)

    while True:
        firstCap = capArr[0]
        combinationFound = False
        newArr = []
        for i in range(1, len(capArr)):
            currentCap = capArr[i]
            if(firstCap + currentCap >= 1000):
                # Valid sum remove both of them
                newArr = capArr[1:]
                beverages += 1
                del newArr[i - 1]
                combinationFound = True
                break

        if not (combinationFound):
            newArr = capArr[1:]

        capArr = newArr

        if(len(capArr) == 0):
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
