import matplotlib.pyplot as plt

### TODO: Answer question in the comments here
# I can observe that the last few numbers in the out, 
# put of each ordered pair are the same for both
#

xlst, ylst = [],[]

def f(n):
    # TODO: IMPLEMENT FUNCTION
    if n%2 == 0:
        return n//2
    else:
        return (3*n)+1

def g(n,i):
    xlst.append(i)
    ylst.append(n)
    print(str(n) + "", end=" ")
    # TODO: IMPLEMENT FUNCTION
    if n == 1:
        return 1
    else:
        return g(f(n), i + 1)

if __name__ == "__main__":
    g(26,0)
    xmax = max(tuple(xlst))
    ymax = max(tuple(ylst))
    print("\nNumber of recursive calls: {0}\nMaximum number: {1}".format(xmax,ymax))
    plt.plot(xlst,ylst,'r--')
    plt.axis([0,xmax,0,ymax])
    plt.show()