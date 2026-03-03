# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
  
  
  i = 0
  for letter in secretWord:
      if letter in lettersGuessed:
          i +=1
      else:
          i = 0
          
  if len(secretWord) != i:
      return False
  else:
    return True
      



def getGuessedWord(secretWord, lettersGuessed):
  

    

    partialWord = ''
    

    for letter in secretWord:
      if letter in lettersGuessed:
          partialWord += letter
      else:
          partialWord += '_ '
    return partialWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global availableLetters
    lettersGuessed = lettersGuessed.lower()
    
    for letter in lettersGuessed:
      if letter in availableLetters:
        availableLetters = availableLetters.replace(letter, "")
    return availableLetters
    
    

def hangman(secretWord):
    global givenLetter 
    global lenghtWord
    global availableLetters
    global lettersGuessed
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    
    
    
    lettersGuessed = ''
    welcome = 'Welcome to the game Hangman!'
    print(welcome)
    lenghtWord = len(secretWord)
    welcomeStatus = 'I am thinking of a word that is '  + str(lenghtWord) + ' letters long.'
    print(welcomeStatus)
   
    
    startTryNumber = 8
    while startTryNumber > 0:
      print("------------")
      startStatus = 'You have ' + str(startTryNumber) + ' guesses left.\nAvailable letters: ' + availableLetters
      print(startStatus)
      givenLetter = input("Please guess a letter: ")
      givenLetter.lower()
      startTryNumber -= 1
      availableLetters = getAvailableLetters(lettersGuessed)
      if givenLetter in availableLetters:
        availableLetters = availableLetters.replace(givenLetter, "")
        if givenLetter in secretWord and not lettersGuessed:       
         
          lettersGuessed = lettersGuessed + givenLetter
          pattern = getGuessedWord(secretWord, lettersGuessed)
          print("Good guess:" + pattern)
         
        elif givenLetter in lettersGuessed:
            pattern = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter:" + pattern)
        else:
          pattern = getGuessedWord(secretWord, lettersGuessed)
          print("Oops! That letter is not in my word:" + pattern)
         
      if isWordGuessed(secretWord, lettersGuessed) == True:
          print("------------")
          print("Congratulations, you won!")
          break
        
    if isWordGuessed(secretWord, lettersGuessed) == False:
      print("------------")
      return ("Sorry, you ran out of guesses. The word was else. ")
     
    
     
    
    
        
        
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
