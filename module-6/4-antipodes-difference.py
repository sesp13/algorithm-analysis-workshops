def getDifference(arr, selectedIndex):
    selectedIndex -= 1
    antipodeIndex = len(arr) - 1 - selectedIndex
    arr = sorted(arr)
    selectedElement = arr[selectedIndex]
    antipodeElement = arr[antipodeIndex]
    print(abs(selectedElement - antipodeElement))


def main():
    inputArr = input().split()
    totalOfElements = int(inputArr[0])
    selectedIndex = int(inputArr[1])

    finalArr = []
    for _ in range(totalOfElements):
        finalArr.append(int(input()))

    getDifference(finalArr, selectedIndex)


main()
