'''
CS Final
Wordle
'''

from colorama import init, Fore, Back, Style
import random
init()


word_list = []
def wordle(attempt):
    Play_Game = 0
    loop = True
    while loop:
        command = input(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit) " + Style.RESET_ALL).lower()
        if command == 'quit':
            loop = False
        elif command == 'y':
            inner_loop = 0
            
            word = random.choice(word_list)
            
            while inner_loop < 5:
                attempt = input('Enter a four letter word: ').upper()
                while len(attempt) != 4:
                    attempt = input('Word was not four letters. Enter another word: ').upper()
                    
                
                output = ''
                for i in range(4): #range is length of word
                    if attempt[i] == word[i]:
                        output = output + Back.GREEN + attempt[i] + Back.RESET
                    elif attempt[i] in word:
                        output = output + Back.YELLOW + attempt[i] + Back.RESET
                    else:
                        output = output + Back.BLACK + attempt[i] + Back.RESET
               
                if word == attempt:
                    inner_loop = inner_loop + 1
                    Play_Game = Play_Game + 1
                    print(f'You win! It took you {inner_loop} guesses and you have played {Play_Game} time(s)')
                    inner_loop = inner_loop + 5 #resets the game
                inner_loop = inner_loop + 1
                
            if inner_loop == 5:
                Play_Game = Play_Game + 1
                print(f'You lost! The correct word was {word}, and you have played {Play_Game} time(s) ')
            
            
if __name__ == '__main__':
    word_list = []
    with open('four_letter.txt', 'r') as fh:
        for line in fh:
            word_list.append(line.strip())
  
    word = random.choice(word_list)
    wordle(word)

