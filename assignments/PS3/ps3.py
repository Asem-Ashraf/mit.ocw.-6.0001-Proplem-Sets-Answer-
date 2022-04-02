# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    new_word = word.lower()
    score_1 = 0
    for letter in new_word:
        score_1 += SCRABBLE_LETTER_VALUES[letter]
    score_2 = 7 * len(new_word) - 3 * (n - len(new_word))
    if score_2 < 1:
        score_2 = 1
    return score_1 * score_2


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():  # this should be iterating over the keys in the hand
        if hand[letter] > 0:  # checks if the letter is not already been removed
            for j in range(hand[
                               letter]):  # this should take the number of times a letter is reapeated and print it that number of times
                print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):  # iterates over the number of the vowels
        x = random.choice(VOWELS)  # chooses a random vowel
        hand[x] = hand.get(x,
                           0) + 1  # assign the number of times the vowel was repeated int the value of the related key
    hand['*'] = 1
    for i in range(num_vowels,
                   n):  # choosing the remaining letters as consonants from the number of vowels to the number of the hand
        x = random.choice(CONSONANTS)  # choosing random consonants
        hand[x] = hand.get(x, 0) + 1  # for repetition

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_word = word.lower()
    new_hand = hand.copy()
    # letter remover code
    for letter in new_word:
        if letter in new_hand:
            if (new_hand[letter] > 0):
                new_hand[letter] = new_hand.get(letter, 0) - 1
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    val1: bool = False
    counter = 0
    new_hand = hand.copy()
    new_word = word.lower()
    if '*' in new_word:
        var = new_word.find('*')  # find the index of the wildcard in the string
        for letter in VOWELS:
            new_new_word = new_word[0:var] + letter + new_word[var + 1:len(
                new_word)]  # assign a vowel to the place of the wildcard character
            if new_new_word in word_list:  # then it searches the word list for that word with different vowels
                val1 = True
                break

    elif new_word in word_list:
        val1 = True
    else:
        return False

    for letter in new_word:
        if letter in new_hand:
            if new_hand[letter] > 0:
                counter += 1
                new_hand[letter] = new_hand.get(letter, 0) - 1

    if (counter == len(new_word)) & val1:
        return True
    else:
        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    val = 0
    for i in hand.keys():
        val += hand[i]
    return val

    pass  # TO DO... Remove this line when you implement this function


def play_hand(hand, word_list, score):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    if calculate_handlen(hand) == 0:
        print('Ran out of letters.')
        return score
    print(' ')
    print('Current Hand: ')
    display_hand(hand)
    word = input('Enter word, or "!!" to indicate that you are finished: ')
    if word == '!!':
        return score
    new_hand = update_hand(hand, word)
    if is_valid_word(word, hand, word_list):
        score += get_word_score(word, calculate_handlen(hand))
        print('"' + word + '" earned', get_word_score(word, calculate_handlen(hand)), 'points.')
        return play_hand(new_hand, word_list, score)
    else:
        print('That is not a valid word.')
        return play_hand(new_hand, word_list, score)
    # ??? ????????? ???
    # SORRY PSEUDOCODE BUT THIS IS RECURSION AT ITS BEST

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is two exclamation points:

    # End the game (break out of the loop)

    # Otherwise (the input is not two exclamation points):

    # If the word is valid:

    # Tell the user how many points the word earned,
    # and the updated total score

    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)

    # update the user's hand by removing the letters of their inputted word

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    newhand = hand.copy()
    letter = ''
    try:
        letter = input('Which letter would you like to replace: ')
        print(' ')
    except:
        print('Enter a letter already in the hand(dont enter *)')
        return substitute_hand(newhand)
    if not letter.isalpha():
        print('Enter a letter already in the hand(dont enter *)input not alphabetical')
        return substitute_hand(newhand)
    if len(letter) > 1:
        print('Enter a letter already in the hand(don\'t enter *)(enter 1 character only)')
        return substitute_hand(newhand)
    letter = letter.lower()

    if letter in newhand.keys():
        repeated = newhand[letter]
        del newhand[letter]
        if letter in VOWELS:
            while (repeated != 0):
                x = random.choice(VOWELS)
                if not x in newhand:
                    newhand[x] = newhand.get(x, 0) + 1
                    repeated -= 1
                else:
                    continue
        elif letter in CONSONANTS:
            while (repeated != 0):
                x = random.choice(CONSONANTS)
                if not x in newhand:
                    newhand.update()
                    newhand[x] = newhand.get(x, 0) + 1
                    repeated -= 1
                else:
                    continue
    else:
        print('Enter a letter already in the hand(don\'t enter *)(charachter not in hand)')
        substitute_hand(newhand)
    return newhand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    def sub(hand):
        try:
            choice: str = input('Would you like to substitute a letter?(yes/no)')
            print(' ')
        except:
            print('Enter "yes" or "no" only')
            sub(hand)
        choice = choice.lower()
        if ((not choice == 'yes') & (not choice == 'no')):
            print('Enter "yes" or "no" only')
            sub(hand)
        if choice == 'yes':
            return substitute_hand(hand)
        elif choice == 'no':
            return hand
        return hand

    hand = {'b':1,'e':2}
        #deal_hand(HAND_SIZE)
    display_hand(hand)
    hand = sub(hand)
    scoree = play_hand(hand, word_list, 0)
    print('Score for this round:', scoree, 'points')
    print('--------------')

    def choise(score):
        choice = input('Would you like to replay the hand? (yes/no)')
        print(' ')
        if (not choice == 'yes') & (not choice == 'no'):
            return choise(score)
        if choice == 'yes':
            score2 = play_hand(hand, word_list, 0)
            print('Total score for this hand:', score2, 'points')
            print('--------------')
            return score2
        elif choice == 'no':
            return score

    scoree = choise(scoree)
    # giving the player the choice to replay the hand

    return scoree


def number_of_hands():
    try:
        return int(input('Enter total number of hands: '))
    except:
        return number_of_hands()

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    # asking the player to select the number of hands to be played
    handss = int(number_of_hands())
    score3 = 0

    for i in range(handss):
        score3 += play_game(word_list)

    print('Total score over all hands:', score3)
#damn, i miss this shit so freakin much man.