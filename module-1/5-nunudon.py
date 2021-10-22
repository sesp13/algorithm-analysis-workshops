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
    if n == 0:
        return 1
    else:
        return n + getDivisors(n)


cases = int(input())
finalArray = []
for i in range(cases):
    arr = [int(x) for x in input().split()]
    finalArray.append(arr)

# Fill the sequence
i = 0
n = 1
counter = 0
numbers = []
while n < 100000:
    while i < n:
        numbers.append(counter)
        i += 1
    counter += 1
    n = getNext(n)

for arr in finalArray:
    n1 = arr[0]
    n2 = arr[1]
    count = abs(numbers[n1 - 1] - numbers[n2])
    print(count)
