from __future__ import print_function
lives = 6
word = ""
letter = ""
updatedSpaces = []
def initialize():
    global word
    global updatedSpaces
    word = "airport"
    print ("_ " * len(word))
    updatedSpaces = ("_ " * len(word))
    print("try to guess the word in less than 6 tries")
    print(updatedSpaces)
def getLetter():
    global letter
    print ("What is your guess")
    letter = raw_input()
#def check():        
def win():
    if updatedSpaces == word:
        print("you won the game!")
    else:
        if lives == 0:
            print("you lost")
def main():
    initialize()
    getLetter()
    #check()
    
     
    
