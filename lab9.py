def fancyString(inVal, correctOutput, funcOutput):
    """
    Returns a string describing what was provided and if values are incorrect or not.

    DOES NOT NEED MODIFIED
    """
    checkCorrect = "Correct = " + u'\u2713'*(funcOutput == correctOutput) + 'X'*(funcOutput != correctOutput)
    # Check mark code from site below:
    # https://stackoverflow.com/questions/16676101/print-the-approval-sign-check-mark-u2713-in-python
    return "Input(s) = {:<15}   Output = {:<25}   Your Output = {:<35}   ".format(str(inVal), str(correctOutput), str(funcOutput)) + checkCorrect


def postitionalSum(list1, list2):
    """ 
    Given 2 lists of the same size, RECURSIVELY add the same positions together
    and return a new list of the same size
    """

    myList = []

    if list1 == []:
        return []
    else:
        myList.append(list1[0]+list2[0])
        list1.remove(list1[0]), list2.remove(list2[0])
        postitionalSum(list1, list2)
    return myList 
    

def palindrome(string):
    """ 
    Recursively returns true if the string is a palindrome. 

    Base case is an empty string (True) or one character (True). Once you know a string is not a palindrome, you can return False.

    Assuming all lowercase letters and there are no spaces

    Not allowed to use list / string iteration i.e. myList[::-1]
    """
    if len(string) <= 1:
        return True
    else:
        

def length(cont):
    """
    Recursively returns the length of the string. Not allowed to use "len"

    Assume input is only a string
    """

    mySum = 0

    if cont == "":
        return 0
    else:
        mySum += 1 + length(cont[1:])
    return mySum
    
        
    
def questionPosedInVideo():
    """
    In the video you had to watch, there was a question asked. 
    Answer it below by returning a string that answers the question.
    """
    return "An iterator is an object that iterates through a sequence="

if __name__ == "__main__":

    if postitionalSum([1], [1]) != None:
        print("Positional Sum")
        print("Positional Sum Tests")
        tests = [
            ([1, 2, 3], [1, 2, 3], [2, 4, 6]),
            ([1, 1, 1], [3, 3, 3], [4, 4, 4]),
            ([-1, 100, 25], [-10, 98, 4], [-11, 198, 29])
        ]

        for t in tests:
            print(fancyString(t[0:2], t[2], postitionalSum(t[0], t[1])))

    if palindrome("") != None:
        print()
        print("Palindrome test")
        tests = [
            ("racecar", True),
            ("melon", False),
            ("tattarrattat", True),
            ("python", False),
            ("a", True),
            ("", True)
        ]
        for t in tests:
            print(fancyString(t[0], t[1], palindrome(t[0])))

    if length("") != None:
        print()
        print("Length Test")

        tests = [
            ("racecar", len("racecar")),
            ("tomato", len("tomato")),
            ("", 0),
            ("a", 1)
        ]
        for t in tests:
            print(fancyString(t[0], t[1], length(t[0])))