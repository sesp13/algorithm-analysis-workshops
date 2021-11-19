def findTheKPair(numbersLength, numbersLst, kIndex):
    numbersLst = sorted(numbersLst)
    numbersLowerThanK, numbersPending = divmod(kIndex, numbersLength)
    numbersLowerThanK = numbersLowerThanK - 1 if(numbersPending == 0) else numbersLowerThanK
    base = numbersLst[numbersLowerThanK]
    sencondPair = numbersLst[numbersPending - 1]
    print("{} {}".format(base, sencondPair))


def main():
    inputArr = [int(x) for x in input().split()]
    numbers = inputArr[0]
    numbersLst = []
    kIndex = inputArr[1]
    for _ in range(numbers):
        numbersLst.append(int(input()))

    findTheKPair(numbers, numbersLst, kIndex)


main()
