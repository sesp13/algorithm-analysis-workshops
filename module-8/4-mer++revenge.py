def solveKnapsack(productsArr, maxWeight):
    # products arr [Cost, Weight]
    productsLength = len(productsArr)
    A = [[0 for __ in range(maxWeight)] for _ in range(productsLength)]

    for i in range(1, productsLength):
        for j in range(maxWeight):
            currentCost = productsArr[i][1]
            prevIndex = i - 1
            if(currentCost <= j):
                currentIncome = productsArr[i][0]
                k = j - currentCost
                A[i][j] = max(currentIncome + A[prevIndex][k], A[prevIndex][k])
            else:
                A[i][j] = A[prevIndex][j]

    return A[-1][-1]


def main():
    numberOfProducts = int(input())
    productsArr = []
    for _ in range(numberOfProducts):
        productsArr.append([int(x) for x in input().split()])

    familyNumber = int(input())

    maxPrice = 0
    for _ in range(familyNumber):
        maxPrice += solveKnapsack(productsArr, int(input()))

    print(maxPrice)


main()
