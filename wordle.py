'''
CS Final
Wordle
'''

'''
CS Final
Wordle
'''

from colorama import init, Fore, Back, Style
import random
import csv
init()

word_list = []

#loop for starting game and continuing it through each guess
loop = True
while loop:
    command = input(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit) " + Style.RESET_ALL).lower()
    if command == 'quit':
        loop = False
    elif command == 'y':
        inner_loop = 0
        word = "LOOP" #random.choice(word_list)
        
        while inner_loop < 5:
            attempt = input('Enter a four letter word: ').upper()
            while len(attempt) != 4:
                attempt = input('Word was not four letters. Enter another word: ').upper()
                
            #game logic
            output = ''
            for i in range(4): #range is length of word
                if attempt[i] == word[i]:
                    output = output + Back.GREEN + attempt[i] + Back.RESET
                elif attempt[i] in word:
                    output = output + Back.YELLOW + attempt[i] + Back.RESET
                else:
                    output = output + Back.BLACK + attempt[i] + Back.RESET
            print(output)
            if word == attempt:
                inner_loop = inner_loop + 1
                print(f'You win! It took you {inner_loop} guesses.')
                inner_loop = inner_loop + 5 #resets the game
            inner_loop = inner_loop + 1
        if inner_loop == 5:
            print(f'You lost! The correct word was {word}.')
            
if __name__ == '__main__':
    with open('four_letter.csv', 'r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word_list.append(float(row[1]))



