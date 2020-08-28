def circuit(A,B,C):
    def Z():
        X = True
        if A and B:
            X = True
        if X or C:
            return True
        else:
            return False
    if not Z() or not C:
        return True
    else:
        return False


#All testing code should be inside this if statement
if __name__=="__main__":

    print(0,0,0,circuit(0,0,0))
    print(0,0,1,circuit(0,0,1))
    print(0,1,0,circuit(0,1,0))
    print(0,1,1,circuit(0,1,1))
    print(1,0,0,circuit(1,0,0))
    print(1,0,1,circuit(1,0,1))
    print(1,1,0,circuit(1,1,0))
    print(1,1,1,circuit(1,1,1))
