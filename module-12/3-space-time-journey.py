import math


def belmanFord(graph: object):
    # Set first node values
    graph['0']['spd'] = 0

    # Set the other spds
    for i in range(len(graph)):
        currentNode = graph[str(i)]
        # See the relations
        for relation in currentNode['related']:
            nextNode = graph[relation[0]]
            currentSum = currentNode['spd'] + relation[1]
            if(currentSum < nextNode['spd']):
                nextNode['spd'] = currentSum

    isPossible = False

    for key in graph:
        currentNode = graph[key]
        # See relations
        for relation in currentNode['related']:
            nextNode = graph[relation[0]]
            currentSum = currentNode['spd'] + relation[1]
            if(currentSum < nextNode['spd']):
                isPossible = True
                break
        if(isPossible):
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
                "related": []
            }

        # Create relations
        for __ in range(wormholes):
            relationArr = input().split()
            origin = relationArr[0]
            destiny = relationArr[1]
            cost = int(relationArr[2])
            # relations structure
            # [destiny, cost]
            inputGraph[origin]['related'].append([destiny, cost])

        finalArr.append(inputGraph)

    for inputGraph in finalArr:
        belmanFord(inputGraph)


main()
