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
def wordle(attempt):
    Play_Game = 0
    loop = True
    while loop:
        command = input(Back.WHITE + Fore.BLACK + "Start a new game? (y/quit) " + Style.RESET_ALL).lower()
        if command == 'quit':
            loop = False
        elif command == 'y':
            inner_loop = 0
            
            
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
                    Play_Game = Play_Game + 1
                    print(f'You win! It took you {inner_loop} guesses and you have played {Play_Game} time(s)')
                    inner_loop = inner_loop + 5 #resets the game
                inner_loop = inner_loop + 1
            if inner_loop == 5:
                Play_Game = Play_Game + 1
                print(f'You lost! The correct word was {word}, and you have played {Play_Game} time(s) ')
            
if __name__ == '__main__':
    with open('four_letter.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["AREA", "ARMY", "BABY", "BALL", "BOOK", "BASE", "CITY", "CARD", "CLUB", "CASE",
             "DATE", "DEAL", "DUTY", "EAST", "EDGE", "FACE", "FACT", "FARM", "FEAR", "FORE", "FILE",
             "FILM", "FISH", "FIRE", "GAME", "GIRL", "GOAL", "GOLD", "HAIR", "HALF", "HAND", "HEAD", "HELD", "HELP", "HOPE",
             "HOUR", "IDEA", "NERD", "KING", "KIND", "LUCK", "LADY", "LIFE", "LIST", "LORD", "LOVE",
             "LASS", "LINK", "MOVE", "MOOD", "MOPE", "NEED", "NEWS", "PAGE", "PAIN", "PARK", "PAST",
             "PATH", "PAIR", "BEAR", "BEAT", "YOUR", "THEY", "THEM", "OURS", "WHEN", "ABLE", "WITH", "UPON",
             "FOUL", "HELL", "CIAO", "DEAD", "WISH", "WANT", "SING", "SONG", "SAVE", "PALE", "HOLY",
             "NAIL", "PAIL", "MAIL", "SANK", "SINK", "ZANY", "MALE", "CAPE", "TAPE", "VENT",
             "RATE", "FATE", "SAND", "DOLL", "PLAY", "UGLY", "RACK", "NEON", "NAME", "QUAD", "QUIZ",
             "SAIL", "SAID", "SALT", "VASE", "WAKE", "WALK", "RUDE", "TEND", "TAXI", "TELL", "CAKE", "SHOP",
             "SHIP", "SOUP", "PLOT", "SPOT", "FIST", "ARCH", "OUCH", "ROCK", "KICK", "SICK", "LICK", "BIRD",
             "BELL", "KILL", "HAND", "FISH", "FROG", "SENT", "TENT", "KISS", "POND", "STOP", "LAMP", "INTO"
             "WORM", "HORN", "DOVE", "LOCK", "HONK", "HARP", "YARN", "DAMP", "JAIL", "CUSS", "WALL",
             "MASK", "PUNK", "MEAT", "DISC", "HERO", "MUSE", "MOON", "STAR", "WORD", "SOUL", "JINX", "EACH", "OOZE", "COZY",
             "ZONE", "YETI", "YAWN", "AXIS", "COAX", "HAVE", "BOXY", "QUIT", "HAZY", "SOIL", "LAZY",
             "SWAN", "SASH", "JADE", "JOLT", "JABS", "JUST", "ICON", "IDOL", "INCH", "INCH", "IDLE",
             "IONS", "OBOE", "OATH", "IRON", "MINE", "KALE", "KELP", "RASP", "RASH", "RICH", "RING", "RIPE", "ROBE"])

    with open('four_letter.csv', 'r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word_list.append(row[1])
    word = random.choice(word_list)
    wordle(word)
    
