# Input value: some number
# Output value: the result of the magical encantation
def magic(x):
#TODO: implement the magical encantation
    x += 15 
    x *= 3
    x -= 9
    x /= 3
    x -= 12
    return x 

if __name__=="__main__":
    #get input
    x = input("Pick any positive whole number: ")
    #change from string to integer
    x = int(x)
    print("Your number was", magic(x))