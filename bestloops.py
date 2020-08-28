def maxFor(xlst):

    #Input Parameter: a list of, possibly empty, numbers x
    #Returns: the max number in list x (does not have to be unique)
    
    highest = 0
    for i in xlst:
        if i == [] or "" or 0:
            return []
        elif i > highest:
            highest = i
    return highest

 
def maxWhile(xlst):
    """
    Input Parameter: a list of, possibly empty, numbers x
    Returns: the max number in list x (does not have to be unique)
    """
    # TODO: implement this function with a while loop
    
    highest = 0
    i = 4
    while i >= 1:
        i = i - 1
        if xlst == [] or "" or 0:
            return []
        elif xlst == False:
            highest = xlst[i]
    return highest

def minFor(xlst):
    """
    Input Parameter: a non-empty list of numbers x
    Returns: the minimal number value in list x (does not have to be unique)
    """
    smallest = 0
    for i in xlst:
        if i < smallest:
            smallest = i
    return smallest

def RemoveEvens(xlst):
    """
    Input Parameters:a list of numbers lst
    Returns: the a new list with all occurrences of evens removed
    """
    for i in xlst:
        if i % 2 == 0:
            xlst.remove(i)
    return xlst

def myReplace(oldX, num, newX, xlst):
    """
    Input Parameters: list that contains either integers or strings
    Return Value: oldX replaced with num copies newX (in a new list)
    """
    # TODO: implement this function

def sumOdd(xlst):
    """
    Input Parameters: list of numbers
    Returns: sum of the odd numbers
    if there are no odd numbers, then print zero
    if the list is empty, print the empty list
    """
    #TODO: implement this function using while
    pass

def StringConcat(xlst):
    """
    Input Parameter: a list x of objects [x1, x2, x3,..., xn]
    Returns: a string that is the concatenation of all the strings
    in the list in order encountered
    """
    s = ""
    s.join(str(xlst))
    return s

if __name__ == "__main__":
    # Data
    w = []
    x = [1,42,24,22,61,100,0,42]
    y = [2]
    z = [555,333,222]
    nlst = [w,x,y,z]
    c = [0,1,1,0,2,1,4]
    a = ["a","b","b", "a", "c","b","e"]
    b = [1,1,2,1,1,2,1,1,2,1,3,1]
    d = ["a",1,"row",0,3,"d","ef",453]

    print("maxFor_____")
    for i in nlst:
        print(maxFor(i))
    print("\nmaxWhile_____")
    for i in nlst:
        print(maxWhile(i))
    print("\nminFor_____")
    for i in nlst:
        print(minFor(i))
    print("\nRemoveEvens_____")
    print(RemoveEvens(b))
    print(RemoveEvens(c))
    print("\nmyReplace_____")
    print(myReplace(1,2,"dog",c))
    print(myReplace(1,2,1,b))
    print("\nsumOdd_____")
    for i in nlst:
        print(sumOdd(i))
    print("\nStringConcat_____")
    print(StringConcat(a))
    print(StringConcat(d))

