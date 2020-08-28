# INPUT income for unmarried
# OUTPUT percent owed as float
# Finish this function
def umt(income):
    if income >= 0 and income <= 9700:
        return float(.10)
    elif income >= 9701 and income <= 39475:
        return float(.12)
    elif income >= 39476 and income <= 84200:
        return float(.22)
    elif income >= 84201 and income <= 160725:
        return float(.24)
    elif income >= 160726 and income <= 204100:
        return float(.32)
    elif income >= 204101 and income <= 510300:
        return float(.35)
    else:
        return float(.37)
#TO DO: Implement Function

# INPUT income for married people
# OUTPUT percent owed as float
# Finish this function
def mt(income):
    if income >= 0 and income <= 19400:
        return float(.10)
    elif income >= 19401 and income <=78950:
        return float(.12)
    elif income >= 78951 and income <= 168400:
        return float(.22)
    elif income >= 168401 and income <= 321450:
        return float(.24)
    elif income >= 321451 and income <= 408200:
        return float(.32)
    elif income >= 408201 and income <= 612350:
        return float(.35)
    else:
        return float(.37)
#TO DO: Implement function

#INPUT income income and marital status Boolean marital_status
#OUTPUT $amount taxes owed
def tax(income, marital_status):
    return income*(umt(income)*(not marital_status) + mt(income) * marital_status)

#All testing code should be inside this if statement
if __name__=="__main__":
    
    ############################
    # DATA
    ############################

    Ursala_married = True
    Ursala_income = 252225
    Kaiser_married = False 
    Kaiser_income = 375000

    Shilah_married = True
    Shilah_income = 77399
    ############################

    print("Ursala owes ", tax(Ursala_income, Ursala_married))
    print("Kaiser owes ", tax(Kaiser_income, Kaiser_married))
    print("Shilah owes ", tax(Shilah_income, Shilah_married))