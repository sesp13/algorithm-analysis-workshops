import queue

# Global vars
globalGraph = {}


def getSubGraph(nodeId):
    global globalGraph

    originNode = globalGraph[nodeId]
    originNode['explored'] = True
    # Init current subgraph
    subgraph = {
        nodeId: originNode
    }
    # Begin with BFS
    register = queue.Queue()
    register.put(originNode)
    while (not register.empty()):
        currentNode = register.get()
        for nextRelation in currentNode['related']:
            nextId = nextRelation[1]
            nextNode = globalGraph[nextId]
            if(nextNode['explored'] == False):
                nextNode['explored'] = True
                subgraph[nextId] = nextNode
                # Update register
                register.put(nextNode)

    return subgraph


def getInfraestructure(arr: list):
    global globalGraph

    globalGraph = arr[0]
    subGraphLst = []

    # Get different graphs
    for nodeId in globalGraph:
        currentNode = globalGraph[nodeId]
        if(currentNode['explored'] == False):
            subGraphLst.append(getSubGraph(nodeId))

    print("Hello World")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        inputArr = [int(x) for x in input().split()]
        cities = inputArr[0]
        possibleConnections = inputArr[1]
        airportCost = inputArr[2]

        inputGraph = {}
        for i in range(1, cities + 1):
            inputGraph[str(i)] = {
                "related": [],
                "explored": False,
            }

        for __ in range(possibleConnections):
            connectionArr = [x for x in input().split()]
            origin = connectionArr[0]
            destiny = connectionArr[1]
            cost = int(connectionArr[2])
            # Relation structure [cost, destiny]
            inputGraph[origin]['related'].append([cost, destiny])
            inputGraph[destiny]['related'].append([cost, origin])

        finalArr.append([inputGraph, inputArr])

    for arr in finalArr:
        getInfraestructure(arr)


main()
