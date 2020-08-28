import numpy as np

np.random.seed(1)

#INPUT array of floats [0,1]
#RETURN average of values
def ave(a):
    # TODO: Implement function
    pass

if __name__ == "__main__":
    
    a = np.random.normal(size = 9).reshape(3,3)

    print(a)
    a_ave = ave(a)
    print("Average = {0}".format(a_ave))
    a = a - a_ave
    print(a)
    print(round(sum(sum(a)),2)) # ?