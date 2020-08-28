from tkinter import *
import random as rn 
window = Tk()
window.geometry('350x350')
window.title("C200")
x = rn.randint(0,100)
y = rn.randint(0,100)
correct, incorrect = 0,0
total = 0

myLabel = Label(window, text="{0}+{1}=".format(x,y), font=("Arial Bold", 15))
myLabel.grid(column=0, row=0)

myLable2 = Label(window, text = "",font=("Arial Bold", 15))
myLable2.grid(column=0, row=5)

mylabel3 = Label(window,text = "{0} out of {1} correct".format(correct, total),font=("Arial Bold", 15)) 
mylabel3.grid(column=0, row=10)

mytxt = Entry(window, width=12)
mytxt.grid(column=1,row=0)

def ClicktheButton1():
    #TODO: Modify this action
    #DO NOT remove anything -- all you need
    #to do is add some elements 

    global x
    global y
    
    global correct
    global incorrect
    global total

    myguess = int(mytxt.get())
  
    if x + y == myguess:
        myLable2.configure(text = "Right!")
        correct += 1
        total += 1
        mylabel3.configure(text = "{0} out of {1} correct".format(correct,total))
    else:
        myLable2.configure(text = "Oops!")
        incorrect += 1
        total +=1
        mylabel3.configure(text = "{0} out of {1} correct".format(correct,total))
  
    
    x = rn.randint(0,100)
    y = rn.randint(0,100)
    mytxt.focus()
    mytxt.delete(0,END)
    myLabel.configure(text = "{0}+{1}=".format(x,y))

btn1 = Button(window, text="check", command = ClicktheButton1)
btn1.grid(column=0, row=7)

def ClicktheButton2():
    window.destroy()

btn1 = Button(window, text="Quit", command = ClicktheButton2)
btn1.grid(column=400, row=400)


window.mainloop()