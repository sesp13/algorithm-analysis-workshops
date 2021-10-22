import math


def isPrime(n):
    if n == 2:
        return True
    else:
        middle = math.ceil(math.sqrt(n))
        for i in range(2, middle + 1):
            if n % i == 0:
                return False
        return True


cases = int(input())
finalArray = []
for i in range(cases):
    arr = [int(x) for x in input().split()]
    finalArray.append(arr)

for arr in finalArray:
    p = arr[0]
    q = arr[1]
    count = 0
    for i in range(p, q + 1):
        if isPrime(i):
            count += 1
    print(count)
