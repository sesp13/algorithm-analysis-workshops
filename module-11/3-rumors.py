from collections import deque


graph = {}


def getRumors(origin):
    global graph

    originNode = graph[origin]
    # No people to tell the rumor
    if(originNode['related'] == []):
        print('0')
        return

    originNode['explored'] = True
    maxDay = 0
    currentDay = 0
    maxDayLength = 0
    register = deque([originNode])
    while (len(register) > 0):
        currentNode = register.pop()
        currentDayLength = 0 if currentNode['day'] == currentDay else currentDayLength
        currentDay = currentNode['day'] + 1

        for nodeId in currentNode['related']:
            nextNode = graph[nodeId]
            if(nextNode['explored'] == False):
                currentDayLength += 1
                nextNode['explored'] = True
                nextNode['day'] = currentDay
                register.append(nextNode)

        if(currentDayLength > maxDayLength):
            maxDayLength = currentDayLength
            maxDay = currentDay

    print(f'{maxDay} {maxDayLength}')

    # Clean graph
    for key in graph:
        graph[key]['explored'] = False
        graph[key]['day'] = 0


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
