# Task 1: Finish the following four functions

def maxThree(x, y, z):
    """
    Returns the maximum of the three parameters
    """
    list1 = [x, y, z]
    list1.sort()
    return(list1[-1])
    # TODO implement this function

    
def minThree(p1, p2, p3):
    """
    Returns the minimum of the three parameters
    """
    list2 = [p1, p2, p3]
    list2.sort()
    return(list2[0])
    # TODO implement this function

    
def maxTwoSum(tomato, potato, idaho):
    """
    Returns the sum of the largest two parameters
    """
    list3 = [tomato, potato, idaho]
    list3.sort()
    summed = list3[-1] + list3[-2]
    return(summed)
    # TODO implement this function
    

def minTwoSum(x, y, z):
    """
    Returns the sum of the smallest two values
    """
    list4 = [x, y, z]
    list4.sort()
    prod = list4[0] + list4[1]
    return(prod)
    # TODO implement this function
    
    
    
# Task 2: Writing more functions
import math

def circleArea(diameter):
    """
    Implement the code in the circle.py listing from Problem 2 of Assignment 1 
    as a function named circleArea that takes in the diameter of a circle and returns the area
    """ 
    radius = float(diameter) / 2 
    return((4/3)*(radius**3)*math.pi)
    # TODO implement this function
    
    
def areaDifference_rect(l1, w1, l2, w2):
    """
    This function takes in the lengths and widths of two different rectangles
    and returns the difference between their two areas
    """
    area1 = l1 * w1
    area2 = l2 * w2
    return(abs(area1 - area2))
    # TODO implement this function
    
    
def areaDifference_circle(d1, d2):
    """
    This function takes in the diameters of two circles and returns    the difference
    between their two areas. Hint: this function can make use of the circleArea function
    """
    return(abs(circleArea(d1) - circleArea(d2)))
    # TODO implement this function


if __name__ == "__main__":
    pass
    #  TODO: Fill me in


#tests
print(maxThree(1,2,3))
print(minThree(1,2,3))
print(maxTwoSum(1,2,3))
print(minTwoSum(1,2,3))
print(circleArea(10))
print(areaDifference_rect(2, 3, 4, 5))
print(areaDifference_circle(10, 20))