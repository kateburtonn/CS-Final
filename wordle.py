'''
Kate Burton & Kaytlyn Lockwood
Computer Programming Final Section G
Wordle
'''

from colorama import init, Fore, Back, Style
import random


word_list = []

def wordle(attempt):
    Play_Game = 0
    #tracks how many times game is played
    loop = True
    while loop:
        start = input(Back.WHITE + Fore.BLACK +
                        'Start a new game? (yes/quit): '
                        + Style.RESET_ALL).lower()
        if start == 'quit':
            loop = False
        elif start == 'yes':
            tries = 0
            #tracks number of attempts
            excueted = []
            #tracks attempted words
            word = random.choice(word_list)
            print(word)
            while tries < 5:
                attempt = input(Back.WHITE + Fore.BLACK +
                                'Enter a four letter word: '
                                + Style.RESET_ALL).upper()
                if attempt in excueted:
                    attempt = input(Back.WHITE + Fore.BLACK +
                                    'Word was already attempted.'
                                    f'Enter another word: '
                                    + Style.RESET_ALL).upper()
                while len(attempt) != 4:
                    attempt = input(Back.WHITE + Fore.BLACK +
                                    'Word was not four letters.'
                                    f' Enter another word: '
                                    + Style.RESET_ALL).upper()
                excueted.append(attempt)     
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
                print(output)
                
                if word == attempt:
                    tries = tries + 1
                    Play_Game = Play_Game + 1
                    print(Back.WHITE + Fore.BLACK +
                          f'You win! It took you {tries} guess(es)'
                          f' and you have played {Play_Game} time(s)'
                          + Style.RESET_ALL)
                    tries = tries + 5 #resets the game
                    
                tries = tries + 1
                #If attempt unsuccessful, adds to counter
                if word != attempt:
                    print(Back.WHITE + Fore.BLACK +
                          f'You have {5 - tries} attempt(s) left.'
                          + Style.RESET_ALL)
                
            if tries == 5:
                Play_Game = Play_Game + 1
                print(Back.WHITE + Fore.BLACK +
                      f'You lost! The correct word was {word},'
                      f' and you have played {Play_Game} time(s)'
                      + Style.RESET_ALL)
            
            
if __name__ == '__main__':
    word_list = []
    with open('four_letter.txt', 'r') as fh:
        for line in fh:
            word_list.append(line.strip())
    #opens word list and appends it
            
    word = random.choice(word_list)
    wordle(word)

