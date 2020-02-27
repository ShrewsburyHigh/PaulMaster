from __future__ import print_function
lives = 6
word = ""
letter = " "
updatedSpaces = []
def initialize():
    global word
    global updatedSpaces
    print("lets play hangman!!")
    word = input("type your word here:")
    lenW = len(word)
    print("try to guess the word in less than 6 tries")
    while lenW != 0:
        updatedSpaces.append('-')
        lenW -=1
    print(updatedSpaces)
def getLetter():
    global letter
    letter = input("type your guess here: ")
    check()
def check():
    # checks the guess that the user makes
    global word
    global lives
    global updatedSpaces
    if letter in word:
        i = (word.find(letter)) 
        del updatedSpaces[i]
        updatedSpaces.insert(i, letter)
        if i != len(word)-1:
            e = (word.find(letter, i+1, len(word) -1))
            if e != -1:
                del updatedSpaces[e]
                updatedSpaces.insert(e, letter)
                if e != len(word)-1:
                    a = word.find(letter, e+1, len(word)+1)
                    if a != -1:
                        del (updatedSpaces[a])
                        updatedSpaces.insert(a, letter)
                else:
                    win()
        else:
            win()
                
    if letter not in word:
        print ('Sorry this letter is not in word')
        lives -= 1
        print ('You have', lives, 'lives left')
        getLetter() 
    print (updatedSpaces[0])
    print (updatedSpaces)
    getLetter()
 
     
def win():
    global lives
    global updatedSpaces
    print (updatedSpaces)
    if '-' not in updatedSpaces:
        print ("CONGRADULATIONS. YOU ARE THE CHAMPION")
        main()

def main():
    initialize()
    getLetter()
    check()
    
main()
    
