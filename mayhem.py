import math

# 1 Finish this function
# Calculates speed from distance and time
# INPUT distance d, time t
# OUTPUT speed 
def speed(d, t):
    return d / t
#TO DO: Implement function

# 2 Finish this function 
# Finds distance using speed and time
# INPUT speed s, time t
# OUTPUT distance
def distance (s, t):
    return s * t
#TO DO: Implement function

# 3 Finish this function
# Finds time using speed and distance
# INPUT speed s, distance d
# OUTPUT time
def time (s, d):
    return d / s
#TO DO: Implement function

# 4 Finish this function
# Converts hours to minutes
# INPUT hours hours
# OUTPUT minutes
def hours_to_min(hours):
    return hours * 60 
#TO DO: Implement function

# 5 Finish this function
# Converts minutes to seconds
# INPUT minutes min
# OUTPUT seconds
def min_to_sec(min):
    return min * 60 
#TO DO: Implement function

# 6 Finish this function
# Converts feet to miles
# INPUT feet feet
# OUTPUT miles
def feet_to_mile(feet):
    return feet / 5280
#TO DO: Implement function

# 7 Finish this function
# Converts miles to kilometers
# INPUT miles miles
# OUTPUT kilometers
def miles_to_kilometers(miles):
    return miles * 1.60934
#TO DO: Implement function

# 8  Finish this function
# Converts kilometers to miles
# INPUT kilometers k
# OUTPUT miles 
def k_to_m(k):
    return k / 1.60934
#TO DO: Implement function

# 9 Finish this function
# Converts miles to feet
# INPUT miles miles
# OUTPUT feet
def miles_to_feet(miles):
    return miles * 5280
#TO DO: Implement function

# 10 Finish this function
# Converts degrees to radians
# INPUT degrees degrees
# OUTPUT radians
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)
#TO DO: Implement function

#11 Finish this function
# Finds the length of side c of a triangle (Law of Cosines)
# where gamma is degrees and is converted to radians
# INPUT side length a, side length b, degree angle gamma
def loc_c(a,b,gamma):
    return math.sqrt((a ** 2) + (b ** 2) - 2 * a * b * math.cos(degrees_to_radians(gamma)))
#TO DO: Implement function

#12 Finish this function
# Convert celcius to fahrenheit 
#INPUT celcius c
#OUTPUT fahrenheit
# 
def c_to_f(celcius):
    return  celcius * (9/5) + 32
#TO DO: Implement function

#13 Finish this function
# Converts fahrenheit to celcius
#INPUT farhenheit fahrenheit
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * (5/9)
#TO DO: Implement function

#13 Finish this function
# Converts fahrenheit to kelvin
#INPUT kelvin kelvin
#OUTPUT fahrenheit
def k_to_f(kelvin):
    return (kelvin - 273.15) * (9 / 5) + 32
#TO DO: Implement function

#14 Finish this function
# Given a stock price p and amount change +/- d, 
# calculate the percentage difference
#INPUT stock price p, dollar amount change v
#OUTPUT percent change
def pc(orig,curr):
    if orig <= curr:
        return ((curr - orig) / orig) * 100
    else:
        return ((orig / curr) / orig) * 100
#TO DO: Implement function

#15 Finish this function
# Convert parsecs to kilometers
#INPUT parsecs p
#OUTPUT kilometers
def p_to_k(parsecs):
    return parsecs * 3.086 * (10 ** 13)
#TO DO: Implement function

#16 Finish this function
# Convert light years to parsecs
#INPUT light years ly
#OUTPUT parsecs
def ly_to_p(lightyear):
    return lightyear / 3.26
#TO DO: Implement function

#All testing code should be inside this if statement
if __name__=="__main__":    
    
    #####################################
    #                                   #
    # DATA                              #
    #####################################
    s1 = 75          # miles/hours
    t1 = 4           # hours
    t2 = 2020        # min
    t3 = 414241      # sec
    d1 = 100         # miles
    d2 = 1442412     # feet
    
    print(speed(d1,t1), "miles/hour")
    print(miles_to_kilometers(speed(d1,t1)), "kilometers/hour")
    print(miles_to_kilometers(speed(d1,t1))/min_to_sec(hours_to_min(1)), "kilometers/sec")
    print(c_to_f(-30), "Fahrenheit")
    print(min_to_sec(hours_to_min(1)), "seconds")
    print(f_to_c(-22), "Celcius")
    print(c_to_f(20), "Fahrenheit")
    print(k_to_f(293), "Fahrenheit")
    print(f_to_c(k_to_f(293)), "Celcius")
    print(loc_c(8,11,37), " units")
    print(degrees_to_radians(30), "radians")
    print(pc(317.69,326.73), "percent change")
    print(p_to_k(231), "kilometers")
    print(k_to_m(p_to_k(ly_to_p(3.5))), "miles")