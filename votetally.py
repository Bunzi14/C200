votes = open("Assignment5/votes.txt","r")

v = votes.readlines()
yes = 0
no = 0


for i in v:
    if i == '1\n':
        yes += 1
    else:
        no += 1

print("Yes",yes,"\n", "No", no)