from bisect import bisect_left


def searchNumber(dbLength, db, number):
    index = bisect_left(db, number)
    if(index != dbLength and db[index] == number):
        print("{} se encuentra en {}".format(number, index + 1))
    else:
        print("{} no se encuentra".format(number))


def main():
    inputArr = [int(x) for x in input().split()]
    dbLength = inputArr[0]
    searchLength = inputArr[1]
    lstNumbers = []
    lstSearch = []
    for _ in range(dbLength):
        lstNumbers.append(int(input()))
    for _ in range(searchLength):
        lstSearch.append(int(input()))

    lstNumbers = sorted(lstNumbers)

    for number in lstSearch:
        searchNumber(dbLength, lstNumbers, number)


main()
