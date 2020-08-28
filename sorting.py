import  random  as rn

xlst = []

for i in  range(rn.randint (1,10)):
    xlst.append ((rn.randint (1 ,100),rn.randint (1 ,100),
        rn.randint (1 ,100)))

print("Original  List")
print(xlst)
print("You can  order  by one of three  dimensions  0,1,2")

x = input("order: ") # This  will be a string  that a"0", "1", or "2".


# Only  changes  go  below

y = lambda order, ylst: eval(order) 
xlst = y(x, xlst)

# Only  changes  go  above
print(xlst)