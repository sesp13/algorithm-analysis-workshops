graph = {}


def getRumors(origin):
    global graph

    originNode = graph[origin]
    # No people to tell the rumor
    if(originNode['related'] == []):
        print('0')
        return

    # Begin with the interaction
    originNode['explored'] = True
    days = [originNode['related']]
    while True:
        originNodes = []
        # Get all valid new origin nodes
        for node in days[-1]:
            if(graph[node]['explored'] == False):
                graph[node]['explored'] = True
                if(node not in originNode):
                    originNodes.append(node)

        # Build next day nodes
        nextNodes = []
        for node in originNodes:
            for newNode in graph[node]['related']:
                if(graph[newNode]['explored'] == False and newNode not in nextNodes):
                    nextNodes.append(newNode)

        if(nextNodes == []):
            break
        else:
            days.append(nextNodes)

    maxDay = []
    for day in days:
        if(len(day) > len(maxDay)):
            maxDay = day

    print(f"{days.index(maxDay) + 1} {len(maxDay)}")

    # Clean graph
    for key in graph:
        graph[key]['explored'] = False


def main():
    global graph

    totalPeople = int(input())
    graph = {}
    for i in range(totalPeople):
        relatedArr = [x for x in input().split()]
        relatedArr = [] if relatedArr[0] == '-1' else relatedArr
        graph[str(i)] = {
            "explored": False,
            "related": relatedArr
        }

    finalArr = [origin for origin in input().split(', ')]

    for origin in finalArr:
        getRumors(origin)


main()
