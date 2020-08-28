import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def getData(fileName):
    """
    TODO: Complete this function

    Given a file path, returns a list of tuples.

    Tuples will be structured as follows:
    [(numAfter1900, population), (numAfter1900, population), ...]

    File will have no header, there will be the following format:
    num num
    num num
    ...
    """
    pass

def P(t):
    #TODO: implement function
    pass

if __name__=="__main__":
    t = np.arange(0.0,120.0) #input to model

    #Get Data From File

    fig, ax = plt.subplots()

    #Complete program that
    #plots data points, the model, and determines
    #the total error that is assigned to variable error
    #the variable error is used in the title, so it
    #must have a value
    #If you have questions about plotting, please
    #refer to Lecture 17 (one of the fun breaks) :)

    #Do not change anything below this line
    ax.set(xlabel='Time (year + 1900)', ylabel=r'Pop. size $\times 10^6$',
        title='Population Growth.  Total model error = {0}'.format(round(error,0)))
    ax.grid()


    fig.savefig("populationgraph.png")
    plt.show()