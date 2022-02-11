def goodBye():
    baseNumber = int(input())

    messages = [
        'Hasta luego curso! Turing, puedes estar orgulloso de mi',
        'Goodbye course! Turing, you can be proud of me',
        'Au revoir cours! Turing, tu peux etre fier de moi',
        'Adeus, curso! Turing, pode se orgulhar de mim',
        'Auf Wiedersehen! Turing, du kannst stolz auf mich sein',
    ]

    while True:
        quotient, remainder = divmod(baseNumber, 5)
        baseNumber = quotient
        print(messages[remainder])
        if(baseNumber < 5):
            break


goodBye()
