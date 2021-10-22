from itertools import permutations


def computeSolutions(inputArr):
    quantity = 0
    n = inputArr[0]
    # case = inputArr[1:]
    # firstSideSum = sum(case[0:4])
    # secondSideSum = case[3:7]
    # thirdSideSum = sum(case[6:]) + case[0]

    # Get all possible number permutations
    numberPermutations = permutations(inputArr[1:])

    # Check every permutation
    for case in numberPermutations:
        firstSideSum = sum(case[0:4])
        secondSideSum = sum(case[3:7])
        thirdSideSum = sum(case[6:]) + case[0]
        if(firstSideSum == n and secondSideSum == n and thirdSideSum == n):
            quantity += 1
    
    print(quantity)


def main():
    cases = int(input())

    for i in range(cases):
        arr = [int(x) for x in input().split()]
        computeSolutions(arr)


main()
