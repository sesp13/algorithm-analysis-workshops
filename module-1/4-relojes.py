def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

cases = int(input())

finalArray = []

for i in range(cases):
    arr = [int(x) for x in input().split()]
    finalArray.append(arr)

for arr in finalArray:
    number1 = arr[0]
    number2 = arr[1]
    number3 = arr[2]
    finalmcd = mcd(number1, number2)
    finalmcd = mcd(finalmcd, number3)
    # The length of the framework is the sum of each number divided by their mcd
    result = (number1 / finalmcd) + (number2 / finalmcd) + ((number3 / finalmcd))
    print(result)
