import math


def getDivisors(n):
    # By default a number always have 2 except for number 1
    if n == 1:
        count = 1
    else:
        count = 2
        middle = math.ceil(n / 2)
        for i in range(2, middle + 1):
            if n % i == 0:
                count += 1

    return count


def getNext(n):
    return n + getDivisors(n)


cases = int(input())
finalArray = []
for i in range(cases):
    arr = [int(x) for x in input().split()]
    finalArray.append(arr)

# Begin the sequence
nSequence = [1]

for arr in finalArray:
    n1 = arr[0]
    n2 = arr[1]
    count = 0

    # Compare with the last one
    if n2 < nSequence[-1]:
        for i in reversed(nSequence):
            if n2 >= i:
                if n1 <= i:
                    count += 1
                else:
                    break
    else:
        # n2 is greater or equal than the last one
        for i in reversed(nSequence):
            if n1 <= i:
                count += 1
            else:
                break
        # Generate the pending items
        while True:
            nextInSequence = getNext(nSequence[-1])
            if nextInSequence <= n2:
                count += 1
                nSequence.append(nextInSequence)
            else:
                break

    print(count)
