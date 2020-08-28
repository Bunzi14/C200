import random as rn
class mastermind:
    numofgues = 0
    answer = ""
    def __init__(self,guess,oldguesses):
        self.guess = guess
        self.oldguesses = oldguesses
    def play(self):
        '''
        TODO: 
            This method will be the kind of like the puppet master of the other methods.The other methods will be helper methods. 
                Here are a few things this method should do
                    - this method should use an input statement to prompt the user to guess again if they can or need to
                    - this method might require some print statements
                    - count the number of times there is a guess
                    - if the person playing has hit 12 guesses then the game should stop and tell them that they have lost
                    - if the person has guessed correctly then stop the game and tell them that
                    - if they are not out of guesses or have won then we need to promt them to guess again after showing them what 
                           they got correct from the last guess
                        -hint: think of a way to do this recursively using a new class object
        '''

        if self.guess == self.answer:
            print("You Got it !")
        else:
            self.numofgues += 1
            testing2 = self.toString(self.guess)
            self.oldguesses += "\n" + testing2
            print(self.oldguesses)
            self.guess = input("enter your guess:")
            if self.numofgues >= 13:
                print("You lost sorry")
                pass
            else:
                self.play()

    def toString(self,pinsinfo):
        '''
        TODO:
            This will be a helper method that returns a string of the guess and how many white pins or black pins they got on that guess
            it will should look something like this  1)  RGRG  b:0  w:1  (hint: use "\n")
                                                     2)  GRYY  b:2  w:0
        '''
        pinscall = self.pins(self.guess)
        blacks = pinscall['black']
        whites = pinscall["white"]

        current = "{}) {} b:{} w:{}".format(self.numofgues, self.guess, blacks, whites )
        return(current)
    
    def pins(self, guess):
        '''
            This helper method will return a list or dictionary of the number of black and white pins a guess got. 
                -White pin: This means their guess had that many colors correct, but they were not in the correct spot
                -Black pin: This means their guess had that many colors correct and in the correct position

                DO NOT CHANGE THIS METHOD
        '''
        colors = ["G","B","Y","R","O","W"]
        anum = {"G":0,"B":0,"Y":0,"R":0,"O":0,"W":0}
        gnum = {"G":0,"B":0,"Y":0,"R":0,"O":0,"W":0}
        black = 0
        white = 0
        g = self.guess
        a = self.answer
        for i in range(0,4):
            if(g[i] == a[i]):
                black += 1
            else:
                anum[a[i]] += 1
                gnum[g[i]] += 1 
        for i in colors:
            if(i in a):
                if(anum[i]<gnum[i]):
                    white += anum[i]
                else:
                    white += gnum[i]
        #now i'm returning the counters as the values
        return {"black":black,"white":white}
    
    def setanswer(self):
        """
        TODO:
            This helper method creates and answer by randomly choosing from the following colors
                - This answer should be four randomly chosen colors as a string (Ex: "GYBW")
                - Then self.answer should be set equal to this answer
        """
        for i in range(4):
            self.answer += rn.choice(colors)

if __name__ == "__main__":
    
    colors = ["G","B","Y","R","O","W"]
    print(colors)
    print("To guess these colors type thier first letter \n LET'S GET STARTED")
    first = str(input("What is your first guess? "))
    test = mastermind(first,"")
    test.setanswer()
    #while testing yourself you might want this
    #print("here is the answer: " , test.answer)
    test.play()
    
