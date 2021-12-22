def getMaxDepatures(arr: list):
    s1 = arr[0]
    s2 = arr[1]
    s1Length = len(s1) + 1
    s2Length = len(s2) + 1
    L = [[0 for __ in range(s2Length)] for _ in range(s1Length)]

    for i in range(1, s1Length):
        prevS1Index = i - 1
        currentS1Element = s1[prevS1Index]
        for j in range(1, s2Length):
            prevS2Index = j - 1
            currentS2Element = s2[prevS2Index]
            if(currentS1Element == currentS2Element):
                L[i][j] = L[prevS1Index][prevS2Index] + 1
            else:
                L[i][j] = max(L[prevS1Index][j], L[i][prevS2Index])

    print(L[-1][-1])


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        finalArr.append([x for x in input().split()])
    for arr in finalArr:
        getMaxDepatures(arr)


main()
