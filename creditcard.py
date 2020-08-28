import math 

APR = float(input("What is you APR : %"))
C = float(input("What is the amount owed on the credit card: $"))
p = float(input("What is the mounthly payment made: $"))
i = (APR/100)/12

n = (-1 * (math.log10(1 - (i * C / p)))) / math.log10(i + 1)

print("You'll make ", math.ceil(n), "Payments.")