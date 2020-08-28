import matplotlib.pyplot as plt
import numpy as np

def readFile(path):
    """
    Read in file and return a list.
    Should be a list of list of pairs of floats
    
    Returns: [[w1, u1], [w2,u2],...,[wn,un]]
    """
    # TODO
    fullFile = open(path, 'r')
    inFile = fullFile.readlines()
    return inFile

def mean(lst):
    """
    Input list of numbers
    Return mean
    """
    #TODO: Implement
    mymean = sum(lst)/len(lst)
    return mymean

def sd(xlst):
    """
    Input list of numbers
    Return the sample variance
    """
    #TODO: Implement
    return np.std(xlst)

def r(x, y):
    """
    Input two lists of numbers
    Return the sample correlation coefficient
    """
    #TODO
    xsd = sd(x)
    ysd = sd(y)
    testing = np.corrcoef(x,y)
    xsv = testing[0][1]
    ysv = testing[1][0]
    rsv = xsv * ysv
    nu = len(x)
    return(rsv / (nu - 1))

if __name__ == "__main__":
    #DATA
    
    # TODO: Read in the file (cannot manually put the data here)

    x = readFile("Assignment10/acme_zyx.txt")
 
    #x1 = [i[0] for i in x]
    #y1 = [i[1] for i in x]
    x1 = [62.5,112,62,122.5,55,75.5,177.5,118.5,59.50,121.5]
    y1 = [85.4,202.55,103.55,202.15,98.9,151.1,181.85,197.3,85.7,195.2]

    rValue = r(x1,y1)

    print(rValue)  
   
    plt.plot(x1,y1, 'ro')
    #TODO: Change the range to fit the data from the file
    # What's the largest value you have for stock and how can you find the largest? (hypothetical)
    # (the function you are thinking about that is 3 letters long is allowed)
    t = np.arange(0,max(x1),.1)
  
    # TODO: Create *your own* best line after inspecting the data
    # You can modify this with trial and error
    # This is a line for the example shown here
    # Your line should be as close to the plots as possible
    # NOTE: We are eyeballing your best guess, there is not an 
    #       exact answer we are looking for
    plt.plot(t,t*1.45 + .5,'g--') 

    # TODO Change the axis to accomodate larger data
    # The x-axis should go a little beyond the largest x value
    # the y-axis should go a little beyond the largest y value
    plt.axis([0,max(x1),0,max(y1)])

    # TODO: Change the xlabel and ylabel
    # to show which stocks are on which axis
    plt.xlabel("Acme Stocks")
    plt.ylabel("ZYX Stocks")


    plt.title("r = {0:.3}".format(rValue))
    plt.savefig("Assignment10/stock.png")
    plt.show()
