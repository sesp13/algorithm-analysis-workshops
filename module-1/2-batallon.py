import math

# Collect data
cases = int(input())
casesArr = []
for i in range(cases):
    casesArr.append(int(input()))

for quantity in casesArr:
    # By defaullt support 2 cases 1 and the number
    count = 2
    maxDistro = math.ceil(quantity / 2)
    for i in range(2, maxDistro + 1):
        if quantity % i == 0:
            count += 1
    print(count)
