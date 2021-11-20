from math import floor


def getBestHouse(arr):
    # Sort array
    arr = sorted(arr)
    arrLength = len(arr)
    middle = floor(arrLength / 2)

    # Get correct index
    index = middle - 1 if arrLength % 2 == 0 else middle
    selectedHouse = arr[index]

    diff = 0
    for element in arr:
        if(element != selectedHouse):
            diff += abs(selectedHouse - element)

    print("{} {}".format(selectedHouse, diff))


def main():
    arrLength = int(input())
    arr = []
    for _ in range(arrLength):
        arr.append(int(input()))

    getBestHouse(arr)


main()
