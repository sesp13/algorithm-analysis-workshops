from itertools import permutations


def getBestCost(numberOfCities, distanceMatrix):
    # By default the best cost is imposible
    bestCost = "imposible"
    # Build an array of cities possitions
    cities = [i for i in range(numberOfCities)]
    # Permute cities array
    citiesPermuted = permutations(cities)

    for city in citiesPermuted:
        totalDistance = 0
        # Iterate the permuted array with indexes
        for i in range(numberOfCities - 1):
            cityPos1 = city[i]
            # filter last case
            # cityPos2 = city[0] if i == numberOfCities - 1 else city[i + 1]
            cityPos2 = city[i + 1]
            # get current distance
            currentDistance = distanceMatrix[cityPos1][cityPos2]
            # Filter invalid combinations
            if(currentDistance == "n.a"):
                totalDistance = "n.a"
                break
            else:
                totalDistance += currentDistance

        if(totalDistance != "n.a"):
            # Fill first valid case
            if(bestCost == "imposible"):
                bestCost = totalDistance / 10
            else:
                # Normal flow
                currentCost = totalDistance / 10
                bestCost = currentCost if currentCost < bestCost else bestCost

    print(bestCost)


def main():
    cases = int(input())
    finalArray = []
    for i in range(cases):
        numberOfCities = int(input())
        distanceMatrix = []
        for city in range(numberOfCities):
            # Parse array value
            lineCase = []
            inputLine = input().split()
            for value in inputLine:
                if value == "n.a":
                    lineCase.append(value)
                else:
                    lineCase.append(int(value))
            distanceMatrix.append(lineCase)

        finalArray.append([numberOfCities, distanceMatrix])

    for case in finalArray:
        getBestCost(case[0], case[1])


main()
