import math
alpha = 1
beta = 1


def palindromize(word):
    global alpha
    global beta
    reversedWord = word[::-1]
    matrixRange = len(word) + 1
    P = [[math.inf for __ in range(matrixRange)]
         for _ in range(matrixRange)]

    # first values
    for i in range(matrixRange):
        P[0][i] = alpha * i
        P[i][0] = alpha * i

    for i in range(1, matrixRange):
        prevI = i - 1
        for j in range(1, matrixRange):
            prevJ = j - 1
            prevValue = P[prevI][prevJ]
            x1 = prevValue + \
                beta if(word[prevI] != reversedWord[prevJ]) else prevValue
            x2 = P[i][prevJ] + alpha
            x3 = P[prevI][j] + alpha

            P[i][j] = min(x1, x2, x3)

    print(int(P[-1][-1] / 2))


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append(input())

    for word in finalArr:
        palindromize(word)


main()
