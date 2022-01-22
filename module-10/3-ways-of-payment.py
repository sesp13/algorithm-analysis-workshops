def howManyWays(arr: list):
    denominations = [1, 2, 5, 10, 20, 50, 100]
    denominationsLength = len(denominations)
    maxItem = max(arr) + 1
    M = [[1 for __ in range(maxItem)] for _ in range(denominationsLength)]

    for i in range(1, denominationsLength):
        for j in range(maxItem):
            prevLineItem = M[i - 1][j]
            if(j < denominations[i]):
                M[i][j] = prevLineItem
            else:
                M[i][j] = prevLineItem + M[i][j - denominations[i]]

    for n in arr:
        print(M[-1][n])


def main():
    arr = []
    while True:
        n = int(input())
        if(n == 0):
            break
        arr.append(n)

    howManyWays(arr)


main()
