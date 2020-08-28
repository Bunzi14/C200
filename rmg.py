def a(n):
    # TODO: Implement recursively
    pass

def ad(n):
    # TODO: Implement bottom-up memoization
    pass

def h():
    # TODO: Implement generator
    pass

#Do not change anything below this line
x = h() #initialize generator do not change

if __name__=="__main__":

    for i in range(0,10):
        print("a({0}) = {1:<4} {2:<4} {3:<4}".format(i,a(i),ad(i), next(x)))