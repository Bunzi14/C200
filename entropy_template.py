import math

#INPUT list of elements
#RETURN list of floats between [0,1] that give the fraction of occurence that sum to one
def makeProbability(xlst):
    # TODO: IMPLEMENT FUNCTION
    pass

#INPUT list of floats that sum to one (probability distribution)
#RETURN entropy   
def entropy(xlst):
    # TODO: IMPLEMENT FUNCTION
    pass

if __name__ == "__main__":
    s1 = ['a','b','a','b','a','b','b','b']
    s2 = [(1),(2),(3),(4)]
    s3 = [1]
    s4 = [1,2]
    xlst = [s1,s2,s3,s4]
    for i in xlst:
        mp = makeProbability(i)
        en = entropy(mp)
        print(en)