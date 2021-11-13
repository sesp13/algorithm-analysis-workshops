from bisect import bisect_left


def findPerfectPair(dbLength, db, numberToSearch):
    index = bisect_left(db, numberToSearch)
    if(index != dbLength and db[index] == numberToSearch):
        print("hay por lo menos una pareja perfecta")
    else:
        if(index == 0):
            nextNumber = db[index]
            print("la pareja mas cercana mide {}".format(nextNumber))
        elif(index == dbLength):
            previousNumber = db[index - 1]
            print("la pareja mas cercana mide {}".format(previousNumber))
        else:
            nextNumber = db[index]
            nextDifference = abs(numberToSearch - nextNumber)
            prevIndex = index - 1
            previousNumber = db[prevIndex]
            previousDifference = abs(numberToSearch - previousNumber)
            if(previousDifference < nextDifference):
                print("la pareja mas cercana mide {}".format(previousNumber))
            elif(previousDifference > nextDifference):
                print("la pareja mas cercana mide {}".format(nextNumber))
            else:
                print("las parejas mas cercanas miden {} y {}".format(
                    previousNumber, nextNumber))


def main():
    inputArr = [int(x) for x in input().split()]
    dbLength = inputArr[0]
    searchLength = inputArr[1]
    lstHeights = []
    lstSearch = []
    for _ in range(dbLength):
        lstHeights.append(int(input()))
    for _ in range(searchLength):
        lstSearch.append(int(input()))

    # Only have unique heights
    lstHeights = sorted(list(set(lstHeights)))
    dbLength = len(lstHeights)

    for number in lstSearch:
        findPerfectPair(dbLength, lstHeights, number)


main()
