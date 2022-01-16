import math


def countDivisors(n):
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if n % i == 0:
            count = count + 1 if n / i == i else count + 2

    return count


def fusion(arr1: list, arr2: list):
    newId = max(arr1[0], arr2[0])
    S = arr1[1] + arr2[1]
    S += countDivisors(S)
    return [newId, S]


def getBestScore(arr: list):
    arrLength = len(arr)
    # Sort arr by id
    arr.sort()
    # Create matrix
    M = [[arr[i] for j in range(arrLength)] for i in range(arrLength)]
    # M = [[[0, 0] for _ in range(arrLength)] for __ in range(arrLength)]

    for matrices in range(1, arrLength):
        for i in range(arrLength - matrices):
            j = i + matrices
            maxItem = [0, 0]
            for k in range(i, j):
                item1 = M[i][k]
                item2 = M[k + 1][j]
                newItem = fusion(item1, item2)
                # Redeclare max
                if(newItem[1] >= maxItem[1]):
                    maxItem = newItem

            M[i][j] = maxItem

    print(M[0][-1][1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        cardsNumber = int(input())
        cardsDeck = []
        for __ in range(cardsNumber):
            cardsDeck.append([int(x) for x in input().split()])

        finalArr.append(cardsDeck)

    for arr in finalArr:
        getBestScore(arr)


main()
