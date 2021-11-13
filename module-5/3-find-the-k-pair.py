def findTheKPair(numbers, numbersLst, kIndex):
    kIndex -= 1
    numbersLst = sorted(numbersLst)
    db = []
    for i in numbersLst:
        for j in numbersLst:
            db.append([i, j])
    selected = db[kIndex]
    print("{} {}".format(selected[0], selected[1]))


def main():
    inputArr = [int(x) for x in input().split()]
    numbers = inputArr[0]
    numbersLst = []
    kIndex = inputArr[1]
    for _ in range(numbers):
        numbersLst.append(int(input()))

    findTheKPair(numbers, numbersLst, kIndex)


main()
