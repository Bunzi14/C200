# Showing some operations with the files

print("Understanding where a file is:")

##############################################################################
"""
Normally, you would put import statements at the top. However, to help under
what is happening, I am putting it with the item I am working with.
"""
import os

"""
This operation is to get the current working directory. This is the location 
the program is looking in the operating system after the program is started. 
"""
path_of_execution = os.getcwd()

"""
This will show the FOLDER you are in, giving you an idea why you might be 
having trouble finding the files you created to read and write.
"""
print("Current location where python program is running: ")
print("\t"+path_of_execution)


##############################################################################
print("\n")
print("Creating a file to read and filling it with gibberish")
fileToWrite = open("playing.txt", "w")
fileToWrite.write("1\n2\n3\n4\n5")
fileToWrite.close()
##############################################################################
print("\n")
print("\t\t READING \t\t")

"""
There are multiple ways to read a file, as such:
"""
print("\n Using read \n")
variableName = open("playing.txt", "r")
contentOfFile = variableName.read()
variableName.close()

print("Contents of the file:")
print("-"*15)
print(contentOfFile, end="")
print("-"*15)

print("\n Using readlines \n")
cof = ""
with open("playing.txt", "r") as variableName2:
    cof = variableName2.readlines()
    print("Raw content:")
    print("\t" + str(cof))


print("Contents of the file:")
print("-"*15)
for c in cof:
    print(c, end="")
print("-"*15)

print("\n Using readline \n")
# I can overwrite the variable since I am not using it
variableName = open("playing.txt", "r") 
contents = ""
currentLine = variableName.readline()
while currentLine != '': # End of file
    contents += currentLine
    currentLine = variableName.readline()
variableName.close()

print("Contents of the file:")
print("-"*15)
print(contents, end="")
print("-"*15)

# Read, readline, and readlines relies on a pointer in the file 
# telling the operating system and Python what line the program 
# is currently seeing

print("\n Using readline and readlines \n")

file = open("playing.txt", "r")
stuff1 = file.readline()
stuff2 = file.readline()
stuff3 = file.readlines()
file.close()

print("Contents of the parts of the file:")
print("-"*15)
print(stuff1, end="")
print("-"*15)
print(stuff2, end="")
print("-"*15)
print(stuff3, end="\n")
print("-"*15)

##############################################################################
print("\n")
print("\t\t WRITING \t\t")
print("\n")

"""
When using just "w" mode in open, this will overwrite the contents of the 
file. 

If you don't want to overwrite the contents, use "a"
"""

stuff = ["a", "b", "c", "d", "e", "f", "g"]

print("\n Writing without newline character \n")

file = open("testing.txt", "w")
file.write("Alphabet")
for s in stuff:
    file.write(s)
file.close()

""" 
If you want to read and write to the same file in Python program,
you MUST close the file (as above). Python lets you get away 
if you forget to close a file, however, will cause problems 
if you try to write after you read the same file (and did not close)
"""

file = open("testing.txt", "r")
print("Contents of the file:")
print("-"*15)
print(file.read(), end="")
print("-"*15)
file.close()


stuff = ["a", "b", "c", "d", "e", "f", "g"]

print("\n Writing WITH newline character \n")

file = open("testing.txt", "w")
file.write("Alphabet\n")
for s in stuff:
    file.write(s + "\n")
file.close()

""" 
If you want to read and write to the same file in Python program,
you MUST close the file (as above). Python lets you get away 
if you forget to close a file, however, will cause problems 
if you try to write after you read the same file (and did not close)
"""

file = open("testing.txt", "r")
print("Contents of the file:")
print("-"*15)
print(file.read(), end="")
print("-"*15)
file.close()

print("\n Writing with writelines \n")

stuffAll = ["Alphabet", "a", "b", "c", "d", "e", "f", "g"]

file = open("testing.txt", "w")
file.writelines(stuffAll)
file.close()

""" 
If you want to read and write to the same file in Python program,
you MUST close the file (as above). Python lets you get away 
if you forget to close a file, however, will cause problems 
if you try to write after you read the same file (and did not close)
"""

file = open("testing.txt", "r")
print("Contents of the file:")
print("-"*15)
print(file.read(), end="")
print("-"*15)
file.close()