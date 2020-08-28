import matplotlib.pyplot as plt
import numpy as np
from correlation import mean, sd, r # This line explained below
"""
The above line will import in the function you complete in 
`correlation.py` (one of the files you are turning in). 
This is example data. You can test that your functions are working. 
"""


if __name__ == "__main__":
    #DATA
    x = [[2,3],[4,3],[1,1.4],[1,.5],[5,3]]
    
    #Splitting the data into x1, y1	
    x1 = [i[0] for i in x]
    y1 = [i[1] for i in x]

    rValue = r(x1,y1)
    print(rValue) 

    plt.plot(x1,y1, 'ro')
    #This is the range to plot (your stock data will be different)
    t = np.arange(0,6,.1)
    #This is my own *estimate* -- you'll have to make one of your own 
    #for the stock data
    plt.plot(t,t*.65 + .5,'g--')
    #This is the grid; you'll have to make a grid that allows you plot
    #all the stock data
    plt.axis([0,6,0,6])
    #You'll have to change the labels to reflect the stock names
    plt.xlabel("A values")
    plt.ylabel("B value")
    plt.title("r = {0:.3}".format(rValue))
    plt.show()