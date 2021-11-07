def getMaxDiscount(caseArr):
    maxDiscount = 0
    numberOfProducts = len(caseArr)
    arrSorted = sorted(caseArr, reverse=True)

    currentIndex = 0
    while True:
        # Evaluate if its posible to set a 3 group
        # The sum is 3 because we have to see if its possible to have the current position plus 2 more
        finalIndex = currentIndex + 3
        if(finalIndex <= numberOfProducts):
            # Sum the value of the item located in the index before than final index
            maxDiscount += arrSorted[finalIndex - 1]
            # Update current index
            currentIndex = finalIndex
        else:
            break

    print(maxDiscount)


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        caseArr = [int(x) for x in input().split()]
        finalArr.append(caseArr)

    for caseArr in finalArr:
        getMaxDiscount(caseArr)


main()
