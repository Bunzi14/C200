#change lat,lon to radians
from math import radians, sin, cos, sqrt, asin 

### TODO: Answer Questions in comments here
# dd would be easier and faster to compute however it would not acount for the earths radius
# I am actaully very suprised at how wrong the answer form the ED is 
# it makes me think that the distance we remeber is only roperly repersented in a 2d manner

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    r = 3961 # radius in miles
    # TODO: Implement function based on the formula above
    latd = (loc2[0] - loc1[0])/2
    lond = (loc2[1] - loc1[1])/2
    d0 = sin(latd)**2 + cos(loc1[0]) * cos(loc2[0]) * sin(lond)**2
    d1 = 2 * r * asin(d0) 
    return d1

def dd(loc1,loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    """
    Euclidian Distance Forumula
    """
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))


if __name__ == "__main__":
    #Lindley Hall where we had C200
    l1 = (39.165341,-86.523588)

    #Luddy Hall the new Luddy building, where we have C200
    l2 = (39.172725,-86.523295)

    #Distance between Lindley and Luddy
    print(hd(l1,l2))
    print(eu_distance(l1,l2))
    print(dd(l1,l2))