moduleComparator = 999999937


def buildFibo(a, b, c, d, n):
    if(n == 1):
        return 1, 1, 1, 0
    elif(n % 2 == 0):
        (a1, b1, c1, d1) = buildFibo(a, b, c, d, n/2)
        tuple1 = (a1 * a1) + (b1 * c1)
        tuple2 = b1 * (a1 + d1)
        tuple3 = c1 * (a1 + d1)
        tuple4 = (d1 * d1) + (b1 * c1)
        return tuple1, tuple2, tuple3, tuple4
    else:
        a1, b1, c1, d1 = buildFibo(a, b, c, d, (n-1)/2)
        tuple1 = (a1 * a1) + (b1 * c1) + b1*(a1 + d1)
        tuple2 = (a1 * a1) + (b1 * c1)
        tuple3 = c1 * (a1 + d1) + (d1 * d1) + (b1 * c1)
        tuple4 = c1 * (a1 + d1)
        return tuple1, tuple2, tuple3, tuple4


def getFibo(n):
    global moduleComparator
    a1, fiboVal, c1, d1 = buildFibo(1, 1, 1, 0, n)
    print(fiboVal % moduleComparator)


def main():
    cases = int(input())
    finalLst = []
    for _ in range(cases):
        finalLst.append(int(input()))

    for n in finalLst:
        getFibo(n)


main()
