#!/usr/bin/python
# -- coding: utf-8 --

'''
games101cards.py
Author: Marcus Guimaraes <mzg218@nyu.edu>
This program is for students taking Games 101 at NYU during Fall 2015 to use for
review purposes.  It takes a plaintext file of the key games (should be packaged
with this program)  and allows users to play flashcards with the info on them.

This is just a simple hack.  No guarantees on its perfection or its elegance.

Written in 2.7 on a Mac.  Working on cross-compatibility.

'''
##TODO: work on Windows compatibility
from random import shuffle
import sys
import io

class Game:
    'represents one of the key games'

    title = ""
    date = ""
    dev = ""
    platform = ""
    region = ""
    
    def __init__(self, title, date, dev, platform, region):
        if title == None or date == None or dev == None or platform == None or \
           region == None:
            print("Error loading " + title)
            exit(-1)
        
        self.title = title.lower().strip()
        self.date = date.lower().strip()
        self.dev = dev.lower().strip()
        self.platform = platform.lower().strip()
        self.region = region.lower().strip()

    def test(self):
        'tests the user on this game'

        elementsCorrect = 0
        
        print(self.title + '\n')

        usrDate = get_input("Date: ").lower()
        #print(usrDate, self.date)
        if usrDate == self.date:
            print("Correct\n")
            elementsCorrect += 1
        elif usrDate.lower() == "exit":
            raise Exception('quit')
        else:
            print("Incorrect -- " + self.date + '\n')

        usrDev = get_input("Developer: ").lower()
        if usrDev == self.dev:
            print("Correct\n")
            elementsCorrect += 1
        elif usrDev.lower() == "exit":
            raise Exception('quit')
        else:
            print("Incorrect -- " + self.dev + '\n')

        usrPlat = get_input("Platform: ").lower()
        if usrPlat == self.platform:
            print("Correct\n")
            elementsCorrect += 1
        elif usrPlat.lower() == "exit":
            raise Exception('quit')
        else:
            print("Incorrect -- " + self.platform + '\n')

        usrReg = get_input("Region of origin: ").lower()
        if usrReg == self.region:
            print("Correct\n")
            elementsCorrect += 1
        elif usrReg.lower() == "exit":
            raise Exception('quit')
        else:
            print("Incorrect -- " + self.region + '\n')

        return elementsCorrect

    def __str__(self):
        return "%s \ndate: %s\ndeveloper: %s\nplatform: %s\nregion of origin: \
%s\n" % (self.title, self.date, self.dev, self.platform, self.region)
    

def main():
    welcome()
    gamesList = createGamesList()
    shuffle(gamesList)
    runTests(gamesList)

def welcome():
    print("Games 101 key game flashcard simulator \n by Marcus Guimaraes \
<mzg218@nyu.edu>\n \n")
    print("Welcome! \n \n")
    print("This script will test your knowledge of the Key Games list. \n")
    print("I made this pretty quickly.  No guarantees on its perfection. \n")
    print("There will probably be cases where your answer is right but the script \
marks it wrong.  Don't take this personally.  Only one keeping score is you.")
    get_input("Press enter to begin.")

def createGamesList():
    '''creates a list of Game objects from a file.  file must be named 
"plaintext key games.txt".  Should be packaged with this program.'''
    print("Loading games.  Please wait...\n")
    
    gamesList = []

    #using io.open for cross-compatibility between python 2 and 3
    fin = io.open('plaintext key games.txt', 'r', encoding='utf-8')
    line = fin.readline()
    while line != '':
        title = line
        date = fin.readline().replace("Date: ", "")
        dev = fin.readline().replace("Developer: ", "")
        platform = fin.readline().replace("Platform: ", "")
        region = fin.readline().replace("Region of Origin: ", "")
        newGame = Game(title, date, dev, platform, region)
        gamesList.append(newGame)
        
        #advance to next game
        line = fin.readline()
        while line == '\n':
            line = fin.readline()

    print("...Done!\n")
    print("%i games loaded\n" % len(gamesList))
    fin.close()
    return gamesList

def runTests(gamesList):
    numToGet = int(get_input("How many elements do you need to get right to get credit? "))
    score = 0
    gamesRun = 0
    print("Enter 'exit' at any time to exit and get stats!\n")
    for game in gamesList:

        print("Game #%i: " % (gamesRun + 1) )
        try:
            partsCorrect = game.test()
        except Exception:
            break
        
        if partsCorrect >= numToGet:
            score += 1
            print("You got credit!\n")
        else:
            print("You did not get credit.\n")

        gamesRun += 1
    print("you got %i game(s) correct out of %i\n" % (score, gamesRun) )

if __name__ == '__main__':
    #TODO: make this more elegant (then we can remove string casts around input)
    #code obtained from: https://triangle717.wordpress.com/tutorials/python/2a3printinput/
    #support input from python 2 and 3
    #default to 3
    get_input = input

    #if this is python 2, use raw_input
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input
        
    main()
    







          
