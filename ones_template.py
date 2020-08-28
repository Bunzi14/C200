import random as rn 


#INPUT List of 0s 1s
#RETURN integer with longest consecutive number of 1s
def lr(xlst):
    # TODO
    pass


if __name__ == "__main__":
    length = rn.randint(1,20)

    x = []

    for i in range(length):
        x.append(rn.randint(0,1))

    print("List of 0s and 1s")
    print(x)

    print("Longest run of 1s")
    print(lr(x))