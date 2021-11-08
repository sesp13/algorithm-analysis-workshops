def compressAlphabet(alphabetArr):
    print(alphabetArr)


def main():
    cases = int(input())
    finalArray = []
    for _ in range(cases):
        numberOfChars = int(input())
        caseArr = []
        for __ in range(numberOfChars):
            arr = input().split()
            arr[1] = int(arr[1])
            caseArr.append(arr)

        finalArray.append(caseArr)

    for alphabetArr in finalArray:
        compressAlphabet(alphabetArr)


main()
