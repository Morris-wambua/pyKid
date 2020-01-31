import random as rand


def rand_Gen():
    number = rand.randrange(0, 10)
    print(number)





def Repeater():
    for x in range(0, 10):
        print(x,rand_Gen())

Repeater()