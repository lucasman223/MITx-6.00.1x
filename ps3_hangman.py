# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in lettersGuessed:
        secretWord = secretWord.replace(char, '')
    if secretWord == "":
        return True
    return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            secretWord = secretWord.replace(char, "_")
    
    return secretWord
    
# =============================================================================
#     one liner for getGuessedWord()
#     return "".join(["_" if char not in lettersGuessed else char for char in secretWord])
# =============================================================================
     
                



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, "")
    return availableLetters
    
# =============================================================================
#     one liner for getAvailableLetters()
#     return "".join(["" if letter in lettersGuessed else letter for letter in availableLetters])
# =============================================================================

def hangman(secretWord):
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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    
    lettersGuessed = []
    guesses = 8
    gameBoard = getGuessedWord(secretWord, lettersGuessed)
    while guesses > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        inp = input("Please guess a letter: ")
        while inp in lettersGuessed:
            print("Oops! You've already guessed that letter: ", gameBoard)
            print("-----------")
            print("You have", guesses, "guesses left")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            inp = input("Please guess a letter: ")
        lettersGuessed.append(inp)
        prevGameBoard = gameBoard
        gameBoard = getGuessedWord(secretWord, lettersGuessed)
        if prevGameBoard == gameBoard:
            print("Oops! That letter is not in my word:", gameBoard)
            guesses -= 1
        else:
            print("Good guess:", gameBoard)
    
    print("-------------")
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord, ".")
    
    return None
    



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#if you type in an input more than 1 letter it will bug
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
