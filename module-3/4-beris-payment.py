berisBank = [
    10000,
    5000,
    1000,
    500,
    100,
    50,
    50,
    10,
    5,
    1,
]


def getMinBerisAmmount(ammount):
    berisCount = 0
    bankCount = 0
    while True:
        if(berisBank[bankCount] <= ammount):
            currentBeris, leftBeris = divmod(ammount, berisBank[bankCount])
            berisCount += currentBeris
            if(leftBeris == 0):
                break
            else:
                ammount = leftBeris
        bankCount += 1

    print(berisCount)


def main():
    cases = int(input())
    finalArr = []
    for i in range(cases):
        finalArr.append(int(input()))

    for amount in finalArr:
        getMinBerisAmmount(amount)


main()
