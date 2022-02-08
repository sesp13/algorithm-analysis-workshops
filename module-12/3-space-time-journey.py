import math


def belmanFord(element: list):
    graph = element[0]
    relations = element[1]

    # Set first node value
    graph['0']['spd'] = 0

    # Set the other spds
    for _ in range(1, len(relations)):
        for relation in relations:
            originNode = graph[relation[0]]
            destinyNode = graph[relation[1]]
            cost = relation[2]
            currentSum = originNode['spd'] + cost
            if(currentSum < destinyNode['spd']):
                destinyNode['spd'] = currentSum

    isPossible = False

    for relation in relations:
        originNode = graph[relation[0]]
        destinyNode = graph[relation[1]]
        cost = relation[2]
        currentSum = originNode['spd'] + cost
        if(currentSum < destinyNode['spd']):
            isPossible = True
            break

    if(isPossible):
        print('es posible viajar al big bang')
    else:
        print('no es posible')


def main():
    cases = int(input())
    finalArr = []

    for _ in range(cases):
        inputArr = input().split()
        solarSystems = int(inputArr[0])
        wormholes = int(inputArr[1])

        # Create graph
        inputGraph = {}
        for i in range(solarSystems):
            inputGraph[str(i)] = {
                "spd": math.inf,
            }

        # Create relations
        relationsArr = []
        for __ in range(wormholes):
            relationArr = input().split()
            # Put as int the cost
            relationArr[2] = int(relationArr[2])
            relationsArr.append(relationArr)

        finalArr.append([inputGraph, relationsArr])

    for element in finalArr:
        belmanFord(element)


main()
