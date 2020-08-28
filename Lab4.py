def what(chevy, gmc, cadillac, buick):
    temp1 = who(chevy, cadillac)
   temp1 * cadillac
    temp1 = temp1 * buick
    return temp1

def who(cat, dog):
    temp1  = 'Abra'
        temp1 = cat * dog
    elif type(cat) == float:
        temp1 = str(temp1) + " is evolving"
    elif type (cat) == list:
        temp1 = "Bayleef"
    else:
        temp1 = dog * cat
    where()
    return temp1

def where():
    temp1 = "Good News Everyone"
    temp2 = ""
    for x in range(len(temp1)):
        k = temp1[x]
        if x >= 2 and x < 6:
            temp2 += k 
    temp2 = temp2 + "ama"
    return temp2

def competitionBracket(age, adultFlag):
    if age > 30 and adultFlag:
        return "Adult Bracket"
    elif age <= 30:
        return "Adult Bracket"
    elif age > 30 and age <= 35:
        return "Master 1 Bracket"
    elif age > 35 and age <= 40:
        return "Master 2 Bracket"
    elif age > 40 and age <= 45:
        return "Master 3 Bracket"


lst = [[1,2], [3,4], [5,6], [7,8]]

def magic(x):
    s = 0 
    for y in x:
        z = y[0]
        s += z 
    return s 

def qinp():
    q = input('Enter a number:')
    if q == 10:
        print('Your number was 10')
    else:
        print('Your number was not 10')


def product(lst):
    # multiplies the two numbers in a two-number list
    first = lst[0]
    second = lst[1]
    product = first * second
    return product
def recProductSum(lst, sum):
    if lst == []:
        return sum
    firstElem = lst[0]
    newSum = sum + product(firstElem)
    restOfList = lst[1:]
    return recProductSum(restOfList, newSum)
        

if __name__ == '__main__':
    print(what("a", 1, 2, 3))
    print(what(1.0, 1, 1, 1))
    print(where())
    print(competitionBracket(36, True))
    print(magic(lst))
    qinp()
    print(recProductSum([[1,2], [3,4], [5,6]], 0))

