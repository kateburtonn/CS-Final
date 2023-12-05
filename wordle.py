'''
Kate Burton & Kaytlyn Lockwood
Computer Programming Final Section G
Wordle
'''

from colorama import Fore, Back, Style
import random


word_list = []


def validation(attempt, executed):
    attempt = input(Back.WHITE + Fore.BLACK +
                                'Enter a four letter word: '
                                + Style.RESET_ALL).upper()
    if attempt in executed:
        attempt = input(Back.WHITE + Fore.BLACK +
                        'Word was already attempted.'
                        ' Enter another word: '
                        + Style.RESET_ALL).upper()
        while attempt in executed:
            attempt = input(Back.WHITE + Fore.BLACK +
                        'Word was already attempted.'
                        ' Enter another word: '
                        + Style.RESET_ALL).upper()
    while len(attempt) != 4:
        attempt = input(Back.WHITE + Fore.BLACK +
                        'Word was not four letters.'
                        ' Enter another word: '
                        + Style.RESET_ALL).upper()
        while attempt in executed:
            attempt = input(Back.WHITE + Fore.BLACK +
                            'Word was already attempted.'
                            ' Enter another word: '
                            + Style.RESET_ALL).upper()
    executed.append(attempt)
    return attempt 

def colorizer(attempt, word):
    output = ''
    for i in range(4): #range is length of word
        if attempt[i] == word[i]:
            output = output + Back.GREEN + attempt[i] + Back.RESET
            #Correct placement
        elif attempt[i] in word:
            output = output + Back.YELLOW + attempt[i] + Back.RESET
            #Correct letter
        else:
            output = output + Back.BLACK + attempt[i] + Back.RESET
            #Incorrect letter
    return output

def playgame(attempt):
    Play_Game = 0 #tracks how many times game is played
    executed = [] #tracks attempted words
    game = True 
    while game: #True starts game, False quits game
        start = input(Back.WHITE + Fore.BLACK +
                        'Start a new game? (yes/quit): '
                        + Style.RESET_ALL).lower()
        if start == 'quit':
            game = False
        elif start == 'yes':
            tries = 0
            #tracks number of attempts
            
            word = random.choice(word_list)
            #chooses a random word for player to guess
            
            while tries < 5:
                
                guess = validation(attempt, executed)
                #calling validated guess into the game
                
                output = colorizer(guess, word)
                #function outputs colorized guess
                #letter in correct spot = green
                #letter in word = yellow
                
                print(output)
                
                if word == guess:
                    tries = tries + 1
                    Play_Game = Play_Game + 1
                    print(Back.WHITE + Fore.BLACK +
                          f'You win! It took you {tries} guess(es)'
                          f' and you have played {Play_Game} time(s)'
                          + Style.RESET_ALL)
                    tries = tries + 5 #resets the game
                    executed = []
                    #clearing list of words attempted for next game
                    
                tries = tries + 1
                #If attempt unsuccessful, adds to counter
                if word != guess:
                    print(Back.WHITE + Fore.BLACK +
                          f'You have {5 - tries} attempt(s) left.'
                          + Style.RESET_ALL)
                
            if tries == 5: #maximum amount of tries
                Play_Game = Play_Game + 1
                print(Back.WHITE + Fore.BLACK +
                      f'You lost! The correct word was {word},'
                      f' and you have played {Play_Game} time(s)'
                      + Style.RESET_ALL)
                
                executed = []
                #clearing list of words attempted for next game
            
if __name__ == '__main__':
    with open('four_letter.txt', 'r') as fh:
        for line in fh:
            word_list.append(line.strip())
            #opens word list and appends it
            
    choice = random.choice(word_list)
    
    playgame(choice)
