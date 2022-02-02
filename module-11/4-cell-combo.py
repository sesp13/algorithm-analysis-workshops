graph = {}
orderedNodes = []
t = 0


def DFS1(nodeId):
    global graph
    global orderedNodes
    global t

    node = graph[nodeId]
    node['explored2'] = True
    for newNodeId in node['related2']:
        newNode = graph[newNodeId]
        if(newNode['explored2'] == False):
            DFS1(newNodeId)

    orderedNodes[t] = nodeId
    t += 1


def DFS2(nodeId):
    global graph

    node = graph[nodeId]
    node['explored'] = True
    for newNodeId in node['related']:
        newNode = graph[newNodeId]
        if(newNode['explored'] == False):
            DFS2(newNodeId)


def getCombos(inputGraph: object):
    global graph
    global orderedNodes
    global t

    graph = inputGraph
    orderedNodes = [None for _ in range(len(graph))]
    t = 0

    for nodeId in graph:
        if(graph[nodeId]['explored2'] == False):
            DFS1(nodeId)

    combos = 0
    orderedNodes.reverse()

    for nodeId in orderedNodes:
        if(graph[nodeId]['explored'] == False):
            DFS2(nodeId)
            combos += 1

    print(combos)


def main():
    finalArr = []
    while True:
        M = int(input())
        if(M == 0):
            break

        inputGraph = {}
        for _ in range(M):
            nameArr = input().split()
            origin = nameArr[0]
            destiny = nameArr[1]
            # Create new nodes
            if(inputGraph.get(origin) == None):
                inputGraph[origin] = {
                    "explored": False,
                    "related": [],
                    "explored2": False,
                    "related2": []
                }
            if(inputGraph.get(destiny) == None):
                inputGraph[destiny] = {
                    "explored": False,
                    "related": [],
                    "explored2": False,
                    "related2": []
                }

            # Add information to the nodes
            inputGraph[origin]["related"].append(destiny)
            inputGraph[destiny]["related2"].append(origin)

        finalArr.append(inputGraph)

    for inputGraph in finalArr:
        getCombos(inputGraph)


main()
