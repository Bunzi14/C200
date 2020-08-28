def vol(x,y,z):
	return x*y*z == 147840

def f(x,y,z):
    # TODO: for a single value of x, y, z, caluclate the value of function "f"
    pass



if __name__ == "main":
    #some arbitrary starting point
    a,b,c = 1,1,1

    # TODO: LOOPS SEARCHING THROUGH all possible 
    #VALUES KEEPING MINIMUM
    # HINT: There should be no print statements in the for loops

    # Do not remove these statements
    print("Smallest dimension possible")
    print("H  W  L  Value")                
    print(a,b,c,f(a,b,c))