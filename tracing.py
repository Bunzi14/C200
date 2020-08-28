def someFunction(dictionary, x, y, z):
    print("Start tracing")
    print()
    def helper(i):
        # Make note of what the value of i (and possible x, y, z) each function call
        print("\tHelper: i={}, x={}, y={}, z={}".format(i, x, y, z))
        if i % 2:
            return x + y + z
        else:
            return x * y * z
    
    for x in range(8, -1, -len(dictionary.keys())):
        h = helper(x)
        print("someFunction: h={}, x={}".format(h, x))
    
    print()
    d = {}
    for x in range(len(dictionary)):
        d[x] = ""
    
    print("someFunction: len(d) = {}".format(len(d)))
    
    # Note what values are happening in the loop
    for i in range(len(d)):
        for k in dictionary:
            d[i] += k[i]
                
    return d
    
    


temp = {
    "blank": "bland", 
    "snack": "slack", 
    "smell": "shell"}

print(someFunction(temp, 2, 3, 4))