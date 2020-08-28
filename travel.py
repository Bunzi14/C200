import  math

def d(s,xdic):
    # TODO: Implement  Function
    mysum = 0.0
    values = []
    for i in s:
        values += i
        if len(values) == 2:
            mysum += (math.sqrt((((xdic[values[0]][0])-(xdic[values[1]][0]))**2) + (((xdic[values[0]][1]) - (xdic[values[1]][1])) **2)))        
            values = values[1:]
    return(mysum)

if  __name__  == "__main__":
    xlst = {}
    with  open("Optional/distance.txt","r") as file:
        for l in file.readlines ():
            k,v = l.strip().split(" ")
            xlst[k] = eval(v) #converts  string  to←↩tuple
    print(xlst)
    print("Travel  {0} = {1}".format("E->B->A->D->C", d("EBADC",xlst)))