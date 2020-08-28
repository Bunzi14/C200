def x(n):
    """
    Implements  the  recursive  function  based  on←↩equations 2 and 3 above.
    """
    
    if n == 0:
        return 4
    else:
        return 2*n-1 + y(n-1)

def y(n):
    """
    Implements  the  recursive  function  based  on←↩equations 4 and 5 above.
    """
    if n == 0:
        return 3
    else:
        return 3*n-2 + x(n-1) 


if  __name__  == "__main__":
    for i in  range (0,10):
        
        print(i,y(i))