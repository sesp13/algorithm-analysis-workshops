def buildKnapsackMatrix(productsArr, maxWeight):
    # products arr [Cost, Weight]
    productsLength = len(productsArr)
    A = [[0 for __ in range(maxWeight + 1)] for _ in range(productsLength + 1)]

    for i in range(1, productsLength + 1):
        prevIndex = i - 1
        currentCost = productsArr[prevIndex][1]
        for j in range(maxWeight + 1):
            prevA = A[prevIndex][j]
            if(currentCost <= j):
                currentIncome = productsArr[prevIndex][0]
                k = j - currentCost
                A[i][j] = max(currentIncome + A[prevIndex][k], prevA)
            else:
                A[i][j] = prevA

    return A


def getMaxPrice(productsArr: list, familyArr: list, maxFamilyWeight: int):
    A = buildKnapsackMatrix(productsArr, maxFamilyWeight)
    s = 0
    for member in familyArr:
        # is A[-1][member] because the matrix has an extra row, column
        s += A[-1][member]
    print(s)


def main():
    numberOfProducts = int(input())
    productsArr = []
    for _ in range(numberOfProducts):
        productsArr.append([int(x) for x in input().split()])

    familyNumber = int(input())
    familyArr = []
    maxFamilyWeight = 0
    for _ in range(familyNumber):
        member = int(input())
        maxFamilyWeight = max(member, maxFamilyWeight)
        familyArr.append(member)

    getMaxPrice(productsArr, familyArr, maxFamilyWeight)


main()
