graph = {}


def getRumors(origin):
    global graph

    # Clean graph
    for dayNumber in graph:
        graph[dayNumber]['explored'] = False
        graph[dayNumber]['day'] = 0

    originNode = graph[origin]
    # No people to tell the rumor
    if(originNode['related'] == []):
        print('0')
        return

    originNode['explored'] = True
    originNode['day'] = 0
    register = [originNode]
    dayGraph = {}
    while (len(register) > 0):
        currentNode = register.pop()
        for nodeId in currentNode['related']:
            nextNode = graph[nodeId]
            if(nextNode['explored'] == False):
                nextNode['explored'] = True
                nextNode['day'] = currentNode['day'] + 1

                # Set day
                if(dayGraph.get(currentNode['day']) == None):
                    dayGraph[currentNode['day']] = 1
                else:
                    dayGraph[currentNode['day']] += 1

                # Update register
                register.append(nextNode)

    # Select max days
    maxDay = 0
    maxDayLength = 0
    for dayNumber in dayGraph:
        dayLength = dayGraph[dayNumber]
        if(dayLength > maxDayLength):
            maxDay = dayNumber
            maxDayLength = dayLength

    print(f'{maxDay + 1} {maxDayLength}')


def main():
    global graph

    totalPeople = int(input())
    graph = {}
    for i in range(totalPeople):
        relatedArr = [x for x in input().split()]
        relatedArr = [] if relatedArr[0] == '-1' else relatedArr
        graph[str(i)] = {
            "explored": False,
            "related": relatedArr,
            "day": 0
        }

    finalArr = [origin for origin in input().strip().split(', ')]

    for origin in finalArr:
        getRumors(origin)


main()
