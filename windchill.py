Temp = float(input("What is the temp outside in F; "))
Vel = float(input("How fast is the wind in MPH; "))

def windChill(T, V):
    return(35.74 + 0.6215 * T - 35.75 * V ** 0.16 + 0.4275 * T * V ** 0.16)
print(windChill(Temp, Vel))
