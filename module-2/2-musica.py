from itertools import combinations


def optimalDuration(array):
    duration = array[0]
    songs = array[1:]

    # First case sum of all songs
    bestDifference = duration - sum(songs)
    if(bestDifference < 0):
        bestDifference = duration
    elif(bestDifference == 0):
        # If the sum is 0 the best combination is possible, dont perform more operations
        print(bestDifference)
        return

    for i in range(1, len(songs)):
        # Get the possible combinations of a song subset of i length
        possibleCombinationsI = combinations(songs, i)
        # Iterate through the iterations
        for comb in possibleCombinationsI:
            difference = duration - sum(comb)
            if(difference >= 0):
                if(difference == 0):
                    # If the sum is 0 the best combination is possible
                    bestDifference = difference
                    break
                elif difference < bestDifference:
                    # Update best difference
                    bestDifference = difference

        if(bestDifference == 0):
            # If the best diffence is 0 dont perform more operations
            break

    # Print the best difference found
    print(bestDifference)


def main():
    cases = int(input())
    finalArray = []
    for i in range(cases):
        arr = [int(x) for x in input().split()]
        finalArray.append(arr)

    for arr in finalArray:
        optimalDuration(arr)


main()
