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

# Fill the sequence
nSequence = [1, 2, 4, 7, 9, 12, 18, 24, 32, 38, 42, 50, 56, 64, 71, 73, 75, 81, 86, 90]
while True:
    nextNumber = getNext(nSequence[-1])
    if nextNumber > 100000:
        break
    else:
        nSequence.append(nextNumber)

for arr in finalArray:
    n1 = arr[0]
    n2 = arr[1]
    count = 0
    index = 0
    while True:
        if nSequence[index] >= n1:
            if nSequence[index] <= n2:
                count += 1
            else:
                break
        index += 1
    print(count)
