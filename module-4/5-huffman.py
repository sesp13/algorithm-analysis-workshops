import heapq


def compressAlphabet(numberOfChars, alphabetArr):
    # Sort array by frecuency
    # alphabetArr = sorted(alphabetArr, key=lambda x: x[1])

    # Priority queque
    queue = []
    heapq.heapify(queue)

    for i in range(numberOfChars):
        element = alphabetArr[i]
        node = {}
        node['char'] = element[0]
        node['freq'] = element[1]
        node['left'] = None
        node['right'] = None
        heapq.heappush(queue, node)

    print(queue)


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

        finalArray.append([numberOfChars, caseArr])

    for alphabetItem in finalArray:
        compressAlphabet(alphabetItem[0], alphabetItem[1])


main()
