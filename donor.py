# allows to pause
import os 

#blood bank type:units
bank = {"A+":5, "A-":6, "O+":4, "O-":2, "B+":5, "B-":6, "AB+":7, "AB-":8}
#blood donor:(recipient1, ..., recipientk)
donorReceiver = {
        "O-":("O-","O+","A+","A-","B+","B-","AB+","AB-"),
        "O+":("O+","A+","B+","AB+"),  
        "A-":("O-","O+","A+","A-",), 
        "A+":("A+","AB+"),
        "B+":("B-","B+","AB+","AB-"),
        "B-":("B-","B+","AB+","AB-"),
        "AB-":("AB+","AB-"),
        "AB+":("AB+") }

def red_blood_compability(donorBloodType):
	"""
	Parameters: donor's blood type (donorBloodType)
	Returns: A tuple of the types that can accept the blood
	"""
	if donorBloodType == "O-":
		return(donorReceiver["O-"])
	elif donorBloodType == "O+":
		return(donorReceiver["O+"])
	elif donorBloodType == "A-":
		return(donorReceiver["A-"])
	elif donorBloodType == "A+":
		return(donorReceiver["A+"])
	elif donorBloodType == "B-":
		return(donorReceiver["B-"])
	elif donorBloodType == "B+":
		return(donorReceiver["B+"])
	elif donorBloodType == "AB-":
		return(donorReceiver["AB-"])
	elif donorBloodType == "AB+":
		return(donorReceiver["AB+"])		

# Show the current bank stock
def showBank():
    print("Current Blood Bank")
    print("{0:>4}  {1:>5}".format("Type","Units"))
    for k,v in bank.items():
        print("{0:>4}  {1:>4}".format(k,v))

#Show number of units of particular type in the bank
def showTypeInBank(bloodType):
    units = bank[bloodType]
    print("{0:>1} units of {1:>2} in bank".format(units, bloodType))


def transfusion(donor, recipient, pints):
	"""
	Parameters:
	- donor: blood type is the donor
	- recipient: blood type of the recipients
	- pints: number of pints the DONOR will give to the recipient using the bank

	Return: 
	- (+1) if the bank has enough AND modify the bank amuont from the donor
	- (0) if either the bank does not have enough of that blood OR the transfer isn't compatible
	"""
	if recipient in red_blood_compability(donor) and bank[donor] >= pints:
		bank[donor] -= pints
		return True
	else:
		return False

###############################
#TESTING 
#Shows current Bank
if __name__ == "__main__":
	showBank()
	input("Press any key to continue")
	#Enough A+==5 units, and 4 can be given to AB+
	#Result is A+==1
	if (transfusion("A+","AB+",4)):
		print("Transfusion successful")
	else:
		print("Transfusion failed")
	showTypeInBank("A+")
	input("Press any key to continue")

	#Fail because O+ cannot donate to B-
	if (transfusion("O+", "B-",1)):
		print("Transfusion successful")
	else:
		print("Transfusion failed")

	#Fail because insufficient units of blood
	if (transfusion("A-","O-",7)):
		print("Transfusion successful")
	else:
		print("Transfusion failed")

	#Succeed and AB-==0 at end
	if (transfusion("AB-","AB+",8)):
		print("Transfusion successful")
	else:
		print("Transfusion failed")
	showTypeInBank("AB-")
	input("Press any key to continue")

	showBank()
