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
    lcm = arr[0]
    for element in arr[1:]:
        lcm = (element * lcm) / mcd(element, lcm)

    print(lcm)
