# Python Class 2344
# Lesson 8 Problem 1 Part (b)
# Author: violet_baudelaire (479380)
from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class Decath1500MFrame(Frame):
    '''frame for a game of 1500 Meters'''

    def __init__(self,master,name):
        '''Decath400MFrame(master,name) -> Decath400MFrame
        creates a new 400 Meters frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and rerolls
        self.scoreLabel = Label(self,text='Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=3,columnspan=2)
        self.rerollLabel = Label(self,text='Rerolls: 5',font=('Arial',18))
        self.rerollLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        # initialize game data
        self.score = 0
        self.rerolls = 5
        self.gameround = 0
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,-6],['black']*5+['red']))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,columnspan=1)
        self.keepButton = Button(self,text='Keep',state=DISABLED,command=self.keep)
        self.keepButton.grid(row=3,columnspan=1)

    def roll(self):
        '''Decath1500MFrame.roll()
        handler method for the roll button click'''
        # roll both dice
        self.dice[self.gameround].roll()
        # if this was the first roll of the round, turn on the keep button
        if self.keepButton['state'] == DISABLED :
            self.keepButton['state'] = ACTIVE
        else:  # otherwise we just spent a reroll
            self.rerolls -= 1
            self.rerollLabel['text'] = 'Rerolls: '+str(self.rerolls)
        if (self.rerolls == 0):  # no rerolls left, so turn off roll button
            self.rollButton['state'] = DISABLED

    def keep(self):
        '''Decath1500MFrame.keep()
        handler method for the keep button click'''
        # add dice to score and update the scoreboard
        self.score += self.dice[self.gameround].get_top()
        self.scoreLabel['text'] = 'Score: '+str(self.score)
        self.gameround += 1  # go to next round
        if self.gameround < 8:  # move buttons to next pair of dice
            self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
            self.keepButton.grid(row=3,column=self.gameround,columnspan=1)
            self.rollButton['state'] = ACTIVE
            self.keepButton['state'] = DISABLED
        else:  # game over
            self.keepButton.grid_remove()
            self.rollButton.grid_remove()
            self.rerollLabel['text'] = 'Game over'

# play the game
name = input("Enter your name: ")
root = Tk()
root.title('1500 Meters')
game = Decath1500MFrame(root,name)
game.mainloop()
#



# Python Class 2344
# Lesson 8 Problem 2
# Author: violet_baudelaire (479380)
from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class ShotPutFrame(Frame):
    '''frame for a game of 1500 Meters'''

    def __init__(self,master,name):
        '''Decath400MFrame(master,name) -> Decath400MFrame
        creates a new 400 Meters frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and rerolls
        self.attemptLabel = Label(self,text='Attempt 1',font=('Arial',18))
        self.attemptLabel.grid(row=0, column=1, columnspan = 2)
        self.scoreLabel = Label(self,text='Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=3,columnspan=2)
        self.highscoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.highscoreLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        # initialize game data
        self.score = 0
        self.highscore = 0
        self.gameround = 0
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll', state= ACTIVE, command=self.roll)
        self.rollButton.grid(row=2,columnspan=1)
        self.foulButton = Button(self, text = 'FOUL', state=DISABLED, command=self.FOUL)
        self.foulButton.grid(row=3,columnspan=1)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=3,columnspan=1)

        self.attempt = 1

    def roll(self):
        '''ShotPutFrame.roll()
        handler method for the roll button click'''
        # roll both dice
        self.dice[self.gameround].roll()
        # if this was the first roll of the round, turn on the keep button
        if self.dice[self.gameround].get_top() == 1:
            self.rollButton['state'] = DISABLED
            self.foulButton['state'] = ACTIVE
            self.stopButton.grid_remove()
            self.scoreLabel.grid_remove()
            self.attemptLabel['text'] = 'FOULED ATTEMPT'
            self.score = 0

        else:

            if self.stopButton['state'] == DISABLED:
                self.stopButton['state'] = ACTIVE
            # add dice to score and update the scoreboard
            self.score += self.dice[self.gameround].get_top()
            self.scoreLabel['text'] = 'Score: '+str(self.score)
            self.gameround += 1  # go to next round
            if self.gameround < 8:  # move buttons to next pair of dice
                self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
                self.stopButton.grid(row=3,column=self.gameround,columnspan=1)
                self.foulButton.grid(row=3,column=self.gameround,columnspan=1)
                self.rollButton['state'] = ACTIVE
            if self.gameround == 8:
                self.rollButton['state'] = DISABLED

    def stop(self):
        '''ShotPutFrame.keep()
        handler method for the keep button click'''
        self.nextround()

    def gameover(self):
        '''Ends the game of shot put'''
        self.stopButton.grid_remove()
        self.rollButton.grid_remove()
        self.foulButton.grid_remove()
        self.highscoreLabel.grid_remove()
        self.scoreLabel.grid_remove()
        self.attemptLabel.grid_remove()
        self.scoreLabel = Label(self, text='Game Over', font=('Arial', 18))
        self.scoreLabel.grid(row=0, column=3, columnspan=2)
        self.highscoreLabel = Label(self, text='Final Score: ' + str(self.highscore), font=('Arial', 18))
        self.highscoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)


    def nextround(self):
        '''Plays the next round of the game'''
        if self.attempt == 3:
            if self.score > self.highscore:
                self.highscore = self.score
            self.gameover()
        else:
            if self.score > self.highscore:
                self.highscore = self.score
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.foulButton.grid_remove()
            self.scoreLabel.grid_remove()
            self.highscoreLabel.grid_remove()
            self.attemptLabel.grid_remove()
            self.attempt += 1
            self.attemptLabel = Label(self, text='Attempt ' + str(self.attempt), font=('Arial', 18))
            self.attemptLabel.grid(row=0, column=1, columnspan=2)
            self.scoreLabel = Label(self, text='Score: 0', font=('Arial', 18))
            self.scoreLabel.grid(row=0, column=3, columnspan=2)
            self.highscoreLabel = Label(self, text='High Score:' + str(self.highscore), font=('Arial', 18))
            self.highscoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)
            # initialize game data
            self.score = 0
            self.gameround = 0
            # set up dice
            self.dice = []
            for n in range(8):
                self.dice.append(GUIDie(self, [1, 2, 3, 4, 5, 6], ['red'] + ['black'] * 5))
                self.dice[n].grid(row=1, column=n)
            # set up buttons
            self.rollButton = Button(self, text='Roll', state=ACTIVE, command=self.roll)
            self.rollButton.grid(row=2, columnspan=1)
            self.foulButton = Button(self, text='FOUL', state=DISABLED, command=self.FOUL)
            self.foulButton.grid(row=3, columnspan=1)
            self.stopButton = Button(self, text='Stop', state=DISABLED, command=self.stop)
            self.stopButton.grid(row=3, columnspan=1)


    def FOUL(self):
        '''ShotPut.FOUL()
        handler method for the FOUL button click'''
        self.nextround()


# play the game

name = input("Enter your name: ")
root = Tk()
root.title('Shot Put')
game = ShotPutFrame(root,name)
game.mainloop()
#



# Python Class 2344
# Lesson 8 Problem 3 Part (a)
# Author: violet_baudelaire (479380)

from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['red']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        if self.top %2 != 0:
            self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=['red'])
            self.color = 'red'
        else:
            self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=['black'])
            self.color = 'black'

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['red']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self,master,valueList=[1,2,3,4,5,6], colorList=['black']*6)
        self.isFrozen = False

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        # you add code here
        return self.isFrozen

    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        # you add code here

        if self.isFrozen:
            self['bg'] = ['white']
            self.isFrozen = False
        elif self.isFrozen == False:
            self['bg'] = ['grey']
            self.isFrozen = True



    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        # you add code here
        if self.isFrozen == False:
            self.top = random.randrange(1,7)
            self.draw()

    def get_top(self):
        return (self.top)

    def get_color(self):
        return self.color



class DiscusFrame(Frame):
    '''frame for a game of 1500 Meters'''

    def __init__(self,master,name):
        '''Decath400MFrame(master,name) -> Decath400MFrame
        creates a new 400 Meters frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and rerolls
        self.attemptLabel = Label(self,text='Attempt 1',font=('Arial',18))
        self.attemptLabel.grid(row=0, column=1, columnspan = 2)
        self.scoreLabel = Label(self,text='Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=3,columnspan=2)
        self.highscoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.highscoreLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        self.directionsLabel = Label(self, text='Click Roll button to Start', font=('Arial',18))
        self.directionsLabel.grid(row=5, column=0, columnspan=5)


        # initialize game data
        self.score = 0
        self.highscore = 0
        # set up dice
        self.dice = []
        for n in range(5):
            self.dice.append(GUIFreezeableDie(self, [1,2,3,4,5,6], colorList= ['red']*6))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll', state= ACTIVE, command=self.roll)
        self.rollButton.grid(row=1, column=6, columnspan=1)
        self.foulButton = Button(self, text = 'FOUL', state=DISABLED, command=self.FOUL)
        self.foulButton.grid(row=2, column=6, columnspan=1)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=2, column= 6, columnspan=1)
        self.freezeButtonone = Button(self, text = 'Freeze', state = DISABLED, command = self.togglefreeze1)
        self.freezeButtonone.grid(row=2, column = 0, columnspan = 1)
        self.freezeButtontwo = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze2)
        self.freezeButtontwo.grid(row=2, column=1, columnspan=1)
        self.freezeButtonthree = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze3)
        self.freezeButtonthree.grid(row=2, column=2, columnspan=1)
        self.freezeButtonfour = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze4)
        self.freezeButtonfour.grid(row=2, column=3, columnspan=1)
        self.freezeButtonfive = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze5)
        self.freezeButtonfive.grid(row=2, column=4, columnspan=1)
        self.attempt = 1
        self.freezedisableone = False
        self.freezedisabletwo = False
        self.freezedisablethree = False
        self.freezedisablefour = False
        self.freezedisablefive = False
        self.trackerone = 0
        self.trackertwo = 0
        self.trackerthree = 0
        self.trackerfour = 0
        self.trackerfive = 0
        self.mandatory = -1

    def roll(self):
        '''ShotPutFrame.roll()
        handler method for the roll button click'''
        self.mandatory += 1

        self.directionsLabel['text'] = 'Click Stop Button to Keep'

        if self.freezedisableone:
            self.trackerone += 1
            self.freezeButtonone['state'] = DISABLED
            self.mandatory = 0
            if self.trackerone == 1:
                self.score += (self.dice[0].get_top())
        if self.freezedisabletwo:
            self.trackertwo += 1
            self.freezeButtontwo['state'] = DISABLED
            if self.trackertwo == 1:
                self.score += (self.dice[1].get_top())
                self.mandatory = 0
        if self.freezedisablethree:
            self.trackerthree += 1
            self.freezeButtonthree['state'] = DISABLED
            if self.trackerthree == 1:
                self.score += (self.dice[2].get_top())
                self.mandatory = 0
        if self.freezedisablefour:
            self.trackerfour += 1
            self.freezeButtonfour['state'] = DISABLED
            if self.trackerfour == 1:
                self.score += (self.dice[3].get_top())
                self.mandatory = 0
        if self.freezedisablefive:
            self.trackerfive += 1
            self.freezeButtonfive['state'] = DISABLED
            if self.trackerfive == 1:
                self.score += (self.dice[4].get_top())
                self.mandatory = 0

        if self.mandatory > 0:
            self.directionsLabel['text'] = 'You must freeze a die to reroll'
        else:
            # roll both dice
            x = []
            z = 0
            active = 0
            record = 0


            for i in range(0,5):
                self.dice[i].roll()
                r = (self.dice[i].get_color())
                q = (self.dice[i].get_top())
                hold = i
                x += [[q,r,hold]]


            # if this was the first roll of the round, turn on the keep button
            for y in x:

                if str(y[1]) == 'red':
                    if x.index(y) == 0:

                        self.freezeButtonone['state'] = DISABLED
                        record += 1
                    if x.index(y) == 1:

                        self.freezeButtontwo['state'] = DISABLED
                        record += 1
                    if x.index(y) == 2:

                        self.freezeButtonthree['state'] = DISABLED
                        record += 1
                    if x.index(y) == 3:

                        self.freezeButtonfour['state'] = DISABLED
                        record += 1
                    if x.index(y) == 4:

                        self.freezeButtonfive['state'] = DISABLED
                        record += 1
                if str(y[1]) == 'black':
                    if x.index(y) == 0:
                        if self.freezedisableone != True:
                            self.freezeButtonone['state'] = ACTIVE
                            active += 1
                    if x.index(y) == 1:
                        if self.freezedisabletwo != True:
                            self.freezeButtontwo['state'] = ACTIVE
                            active += 1
                    if x.index(y) == 2:
                        if self.freezedisablethree != True:
                            self.freezeButtonthree['state'] = ACTIVE
                            active += 1
                    if x.index(y) == 3:
                        if self.freezedisablefour != True:
                            self.freezeButtonfour['state'] = ACTIVE
                            active += 1

                    if x.index(y) == 4:
                        if self.freezedisablefive != True:
                            self.freezeButtonfive['state'] = ACTIVE
                            active += 1

        if active == 0:
            self.rollButton['state'] = DISABLED
            self.foulButton['state'] = ACTIVE
            self.stopButton.grid_remove()
            self.scoreLabel.grid_remove()
            self.attemptLabel['text'] = 'FOULED ATTEMPT'
            self.score = 0
            self.directionsLabel['text']='Click FOUL to Continue'

        if record == 5:
            self.rollButton['state'] = DISABLED
            self.foulButton['state'] = ACTIVE
            self.stopButton.grid_remove()
            self.scoreLabel.grid_remove()
            self.attemptLabel['text'] = 'FOULED ATTEMPT'
            self.score = 0
            self.directionsLabel['text']='Click FOUL to Continue'
        else:

            if self.stopButton['state'] == DISABLED:
                self.stopButton['state'] = ACTIVE
            self.scoreLabel['text'] = 'Score: '+str(self.score)

    def togglefreeze1(self):
        self.dice[0].toggle_freeze()
        self.freezedisableone = not self.freezedisableone


    def togglefreeze2(self):
        self.dice[1].toggle_freeze()
        self.freezedisabletwo = not self.freezedisabletwo


    def togglefreeze3(self):
        self.dice[2].toggle_freeze()
        self.freezedisablethree = not self.freezedisablethree


    def togglefreeze4(self):
        self.dice[3].toggle_freeze()
        self.freezedisablefour = not self.freezedisablefour


    def togglefreeze5(self):
        self.dice[4].toggle_freeze()
        self.freezedisablefive = not self.freezedisablefive





    def stop(self):
        '''ShotPutFrame.keep()
        handler method for the keep button click'''
        if self.freezedisableone:
            self.trackerone += 1
            self.freezeButtonone['state'] = DISABLED
            if self.trackerone == 1:
                self.score += (self.dice[0].get_top())
        if self.freezedisabletwo:
            self.trackertwo += 1
            self.freezeButtontwo['state'] = DISABLED
            if self.trackertwo == 1:
                self.score += (self.dice[1].get_top())
        if self.freezedisablethree:
            self.trackerthree += 1
            self.freezeButtonthree['state'] = DISABLED
            if self.trackerthree == 1:
                self.score += (self.dice[2].get_top())
        if self.freezedisablefour:
            self.trackerfour += 1
            self.freezeButtonfour['state'] = DISABLED
            if self.trackerfour == 1:
                self.score += (self.dice[3].get_top())
        if self.freezedisablefive:
            self.trackerfive += 1
            self.freezeButtonfive['state'] = DISABLED
            if self.trackerfive == 1:
                self.score += (self.dice[4].get_top())
        self.nextround()




    def gameover(self):
        '''Ends the game of shot put'''
        self.stopButton.grid_remove()
        self.rollButton.grid_remove()
        self.foulButton.grid_remove()
        self.highscoreLabel.grid_remove()
        self.scoreLabel.grid_remove()
        self.attemptLabel.grid_remove()
        self.directionsLabel.grid_remove()
        self.scoreLabel = Label(self, text='Game Over', font=('Arial', 18))
        self.scoreLabel.grid(row=0, column=3, columnspan=2)
        self.highscoreLabel = Label(self, text='Final Score: ' + str(self.highscore), font=('Arial', 18))
        self.highscoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)


    def nextround(self):
        '''Plays the next round of the game'''
        if self.attempt == 3:
            if self.score > self.highscore:
                self.highscore = self.score
            self.gameover()
        else:
            if self.score > self.highscore:
                self.highscore = self.score
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.foulButton.grid_remove()
            self.scoreLabel.grid_remove()
            self.highscoreLabel.grid_remove()
            self.attemptLabel.grid_remove()
            self.directionsLabel.grid_remove()
            self.freezedisableone = False
            self.freezedisabletwo = False
            self.freezedisablethree = False
            self.freezedisablefour = False
            self.freezedisablefive = False
            self.trackerone = 0
            self.trackertwo = 0
            self.trackerthree = 0
            self.trackerfour = 0
            self.trackerfive = 0
            self.attempt += 1
            self.mandatory = -1
            self.score = 0
            self.attemptLabel = Label(self, text='Attempt '+ str(self.attempt), font=('Arial', 18))
            self.attemptLabel.grid(row=0, column=1, columnspan=2)
            self.scoreLabel = Label(self, text='Score: ' + str(self.score), font=('Arial', 18))
            self.scoreLabel.grid(row=0, column=3, columnspan=2)
            self.highscoreLabel = Label(self, text='High Score: ' + str(self.highscore), font=('Arial', 18))
            self.highscoreLabel.grid(row=0, column=5, columnspan=3, sticky=E)
            self.directionsLabel = Label(self, text='Click Roll button to Start', font=('Arial', 18))
            self.directionsLabel.grid(row=5, column=0, columnspan=5)
            # initialize game data

            # set up dice
            self.dice = []
            for n in range(5):
                self.dice.append(GUIFreezeableDie(self, [1, 2, 3, 4, 5, 6],
                                                  ['red'] + ['black'] + ['red'] + ['black'] + ['red'] + ['black']))
                self.dice[n].grid(row=1, column=n)
            # set up buttons
            self.rollButton = Button(self, text='Roll', state=ACTIVE, command=self.roll)
            self.rollButton.grid(row=1, column=6, columnspan=1)
            self.foulButton = Button(self, text='FOUL', state=DISABLED, command=self.FOUL)
            self.foulButton.grid(row=2, column=6, columnspan=1)
            self.stopButton = Button(self, text='Stop', state=DISABLED, command=self.stop)
            self.stopButton.grid(row=2, column=6, columnspan=1)
            self.freezeButtonone = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze1)
            self.freezeButtonone.grid(row=2, column=0, columnspan=1)
            self.freezeButtontwo = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze2)
            self.freezeButtontwo.grid(row=2, column=1, columnspan=1)
            self.freezeButtonthree = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze3)
            self.freezeButtonthree.grid(row=2, column=2, columnspan=1)
            self.freezeButtonfour = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze4)
            self.freezeButtonfour.grid(row=2, column=3, columnspan=1)
            self.freezeButtonfive = Button(self, text='Freeze', state=DISABLED, command=self.togglefreeze5)
            self.freezeButtonfive.grid(row=2, column=4, columnspan=1)


    def FOUL(self):
        '''ShotPut.FOUL()
        handler method for the FOUL button click'''
        self.nextround()





# test application
name = input("Enter your name: ")
root = Tk()
root.title('Discus')
game = DiscusFrame(root,name)
game.mainloop()