import heapq


def iterateTree(digit='', structure={}):
    if(structure == -1):
        return

    digit += structure['digit']
    leftNode = structure['left']
    rightNode = structure['right']

    if(leftNode == -1):
        print("{} {}".format(structure['char'], digit))
    else:
        iterateTree(digit, leftNode)

    # Only check right node if leftNode
    if(rightNode == -1 and leftNode != -1):
        print("{} {}".format(structure['char'], digit))
    else:
        iterateTree(digit, rightNode)


def compressAlphabet(numberOfChars, alphabetArr):
    # Sort array by frecuency
    # alphabetArr = sorted(alphabetArr, key=lambda x: x[1])

    # Priority queque
    queue = []
    heapq.heapify(queue)

    # Create all nodes for the tree
    for i in range(numberOfChars):
        letter = alphabetArr[i]
        node = [-1, i, -1]
        dictObject = {}
        dictObject['char'] = letter[0]
        dictObject['left'] = -1
        dictObject['right'] = -1

        # Build Node
        # [0: frecuency, 1: i counter this is used to solve ties in heapq, 2: structure]
        node[0] = letter[1]
        node[2] = dictObject

        # Add node to the queue
        heapq.heappush(queue, node)

    # Begin the filter of the tree
    for _ in range(numberOfChars - 1):
        node = [-1, -1, -1]
        dictObject = {}
        nodeLeft = heapq.heappop(queue)
        nodeRight = heapq.heappop(queue)
        nodeLeft[2]['digit'] = '0'
        nodeRight[2]['digit'] = '1'
        dictObject['left'] = nodeLeft[2]
        dictObject['right'] = nodeRight[2]
        dictObject['char'] = dictObject['left']['char'] + \
            dictObject['right']['char']
        newFrecuency = nodeLeft[0] + nodeRight[0]

        # Build new node
        # [0: frecuency, 1: right counter (which is bigger) this is used to solve ties in heapq, 2: structure]
        node[0] = newFrecuency
        node[1] = nodeRight[1]
        node[2] = dictObject

        # Add node to the queue
        heapq.heappush(queue, node)

    # Get decision tree
    tree = heapq.heappop(queue)[2]

    iterateTree('', tree['left'])
    iterateTree('', tree['right'])


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

    for i in range(len(finalArray)):
        print("caso {}:".format(i + 1))
        alphabetItem = finalArray[i]
        compressAlphabet(alphabetItem[0], alphabetItem[1])
        print("")


main()
