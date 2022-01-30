currentGraph = {}
currentFamily = []


def checkMembers(key):
    global currentGraph
    global currentFamily

    register = [key]
    while(len(register) != 0):
        node = register.pop()
        if(currentGraph[node]['explored'] == True):
            continue
        else:
            currentGraph[node]['explored'] = True
            if (node not in currentFamily):
                currentFamily.append(node)
            # Go on with related
            for newNode in currentGraph[node]['related']:
                if(currentGraph[newNode]['explored'] == False):
                    register.append(newNode)


def getInfo(graph: object):
    global currentGraph
    global currentFamily

    currentGraph = graph
    families = []
    for key in graph:
        currentNode = graph[key]
        if(currentNode['explored'] == False):
            currentFamily = []
            checkMembers(key)
            families.append(currentFamily)

    maxNumber = 0
    for family in families:
        maxNumber = max(maxNumber, len(family))

    print(f"{len(families)} {maxNumber}")


def main():
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        R = int(input())
        graph = {}
        for __ in range(R):
            register = [x for x in input().split()]

            # Add new nodes to the graph
            if(graph.get(register[0]) == None):
                graph[register[0]] = {
                    "explored": False,
                    "related": []
                }

            if(graph.get(register[1]) == None):
                graph[register[1]] = {
                    "explored": False,
                    "related": []
                }

            # Update related nodes in the graph
            related1 = graph[register[0]]['related']
            related2 = graph[register[1]]['related']

            if(register[1] not in related1):
                related1.append(register[1])

            if(register[0] not in related2):
                related2.append(register[0])

        finalArr.append(graph)

    for graph in finalArr:
        getInfo(graph)


main()
