# Problem Set 2, hangman.py
# Name: Asem Ashraf Abd El-Ghafar Sharaf El-Deen
# Collaborators: none
# Time spent: 6 and half hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def chooseSecretWord(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, allGuessedLettersList):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # we should iterate over the secret word using for loop i in range secret_word
    # the we should compare each guessed letter with the current selected letter of the 
    # secret word that should do it but it  is not the most efficient
    # efficiency would be like removing the letters that is in the secret word from the 
    # guessed list but what if the letter is repeated in the secret word it wont detect
    # the way we do this is by nested for loop. one iterates over secret word and the 
    # other over the guessed list simple but we will use recursion. if the comparision is
    # false then we recall the function in the next index otherwise we return true
    # this is the tricky part we use a counter for the correctly guessed letters 
    # if they are the same as the secret word length then we return true if not then false
    counter = 0
    for letterInSecretWord in secret_word :
        for guessedLetter in allGuessedLettersList :
            if guessedLetter==letterInSecretWord :
                counter+=1
                break

    return len(secret_word)==counter
                



def get_guessed_word(secret_word, correctlyGuessedLettersList, special = False):
    '''
    secret_word: string, the word the user is guessing
    correctlyGuessedLettersList: list (of letters), which letters have been guessed so far
    special : ture if i dont want a space after the undercore (this keeps the length of the word the same)
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secretWordWithDashes = ''
    for letterInSecretWord in secret_word :
        counter = 0
        for correctlyGuessedLetter in correctlyGuessedLettersList :
            counter+=1
            if correctlyGuessedLetter==letterInSecretWord :
                secretWordWithDashes += correctlyGuessedLetter
                break
            elif counter == len(correctlyGuessedLettersList):
                if special :
                    secretWordWithDashes += '_'
                else:
                    secretWordWithDashes += '_ '
                break
            
    return secretWordWithDashes


def correctlyGuessedLetters(secretWord, allGuessedLettersList):
    '''
       returns a list of correctly guessed letters
    '''
    correct_guesses = []
    for letterInSecretWord in secretWord :
        for guessedLetter in allGuessedLettersList :
            if guessedLetter==letterInSecretWord :
                correct_guesses.append(guessedLetter)
                break
    return correct_guesses



def get_available_letters(allGuessedLettersList):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabete = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for guessedLetter in allGuessedLettersList :
        alphabete.remove(guessedLetter)

    return ''.join(alphabete)
    
    

# -----------------------------------


def match_with_gaps(my_word, other_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word)==len(other_word):
        if get_guessed_word(other_word,correctlyGuessedLetters(other_word, letters_guessed))== get_guessed_word(my_word,letters_guessed):
            print (other_word + ' ')
            return True 
    return False

def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for other_word in wordlist:
        match_with_gaps(my_word,other_word, letters_guessed)

def hangman(secretWord, hints=False):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    counter = 0
    guessedLettersList=[]
    remainingGuessesCount=6
    remainingWarningsCount=3
    secretWordLetterCount = len(secretWord)
    dash = '----------------------------------------------------'

    def lost():
        return remainingGuessesCount<=0
    def OutOfWarnings():
        return remainingWarningsCount<=0

    if hints:
        print('Welcome to the game Hangman! (with hints)')
    else:
        print('Welcome to the game Hangman! (without hints)')

    print('I am thinking of a word that is' , secretWordLetterCount , 'letters long. ')
    print(dash)
    
    while remainingGuessesCount >0:
        print ('You have', remainingGuessesCount , 'guesses left.')
        print ('Available letters: ' + get_available_letters(guessedLettersList))
        print ('Please guess a letter: ')
        lastGuessedLetter = input()
        if str.isalpha(lastGuessedLetter):
            lastGuessedLetter = str.lower(lastGuessedLetter)
            if lastGuessedLetter in guessedLettersList :
                if OutOfWarnings():
                    if lost():
                        break
                    print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess.')
                    remainingGuessesCount-=1
                else:
                    remainingWarningsCount-=1
                    if lost():
                        break
                    print ('Oops! You\'ve already guessed that letter. You have ', remainingWarningsCount,' warnings left.')

                print(get_guessed_word(secretWord, guessedLettersList))
            elif lastGuessedLetter in secretWord :
                counter+=1
                guessedLettersList.append(lastGuessedLetter)
                print ('Good guess.')
                print(get_guessed_word(secretWord, guessedLettersList))
                if get_guessed_word(secretWord, guessedLettersList)==secretWord :
                    print(dash)
                    break
            else :
                guessedLettersList.append(lastGuessedLetter)
                if lastGuessedLetter in ['a','i','o','u','e'] :
                    remainingGuessesCount-=2
                    print ('Oops! That letter is not in my word.')
                    print(get_guessed_word(secretWord, guessedLettersList))
                    if lost():
                        break
                else :
                    remainingGuessesCount-=1
                    print ('Oops! That letter is not in my word.')
                    print(get_guessed_word(secretWord, guessedLettersList))
                    if lost():
                        break
        elif (lastGuessedLetter == '*')&hints:
            show_possible_matches(get_guessed_word(secretWord, guessedLettersList, True),guessedLettersList)
        else :
            remainingWarningsCount-=1
            if lost():
                break
            print ('Oops! That is not a valid letter. You have ', remainingWarningsCount ,' warnings left.')
            print(get_guessed_word(secretWord, guessedLettersList))

        print(dash)

    if lost():
         print('Sorry, you ran out of guesses. The word was',secretWord,'.')
    else:
         print('Congratulations, you won!')
         print('Your total score for this game is:',remainingGuessesCount*counter)

def GetChoice(secretWord):
    HintsChoice = input().lower()
    if HintsChoice == 'a':
        hangman(secretWord,hints=True)
    elif HintsChoice == 'b':
        hangman(secretWord,hints=False)
    else :
        print('INVALID INPUT. ENTER (a) OR (b).')
        GetChoice(secretWord )


print('Welcome to the word guessing game. Hangman.')
print('This game was developed as a part of MIT 6.0001 course according to the specifications in PS2')
print('Play hangman with hints. Press (a).\nPlay hangman without hints. Press (b).')

GetChoice(chooseSecretWord(wordlist))
