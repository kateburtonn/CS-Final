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

"""
word_list = ["AREA\n" "ARMY\n" "BABY\n" "BALL\n" "BOOK\n" "BASE\n" "CITY\n" "CARD\n"
             "CLUB\n" "CASE\n" "DATE\n" "DEAL\n" "DUTY\n" "EAST\n" "EDGE\n" "FACE\n" "FACT\n" "FARM\n"
             "FEAR\n" "FORE\n" "FILE\n" "FILM\n" "FISH\n" "FIRE\n" "GAME\n" "GIRL\n" "GOAL\n" "GOLD\n" "HAIR\n" "HALF\n"
             "HAND\n" "HEAD\n" "HELD\n" "HELP\n" "HOPE\n"
             "HOUR\n" "IDEA\n" "NERD\n" "KING\n" "KIND\n" "LUCK\n" "LADY\n" "LIFE\n" "LIST\n" "LORD\n" "LOVE\n"
             "LASS\n" "LINK\n" "MOVE\n" "MOOD\n" "MOPE\n" "NEED\n" "NEWS\n" "PAGE\n" "PAIN\n" "PARK\n" "PAST\n"
             "PATH\n" "PAIR\n" "BEAR\n" "BEAT\n" "YOUR\n" "THEY\n" "THEM\n" "OURS\n" "WHEN\n" "ABLE\n" "WITH\n" "UPON\n"
             "FOUL\n" "HELL\n" "CIAO\n" "DEAD\n" "WISH\n" "WANT\n" "SING\n" "SONG\n" "SAVE\n" "PALE\n" "HOLY\n"
             "NAIL\n" "PAIL\n" "MAIL\n" "SANK\n" "SINK\n" "ZANY\n" "MALE\n" "CAPE\n" "TAPE\n" "VENT\n"
             "RATE\n" "FATE\n" "SAND\n" "DOLL\n" "PLAY\n" "UGLY\n" "RACK\n" "NEON\n" "NAME\n" "QUAD\n" "QUIZ\n"
             "SAIL\n" "SAID\n" "SALT\n" "VASE\n" "WAKE\n" "WALK\n" "RUDE\n" "TEND\n" "TAXI\n" "TELL\n" "CAKE\n" "SHOP\n"
             "SHIP\n" "SOUP\n" "PLOT\n" "SPOT\n" "FIST\n" "ARCH\n" "OUCH\n" "ROCK\n" "KICK\n" "SICK\n" "LICK\n" "BIRD\n"  
             "BELL\n" "KILL\n" "HAND\n" "FISH\n" "FROG\n" "SENT\n" "TENT\n" "KISS\n" "POND\n" "STOP\n" "LAMP\n" "INTO\n"
             "WORM\n" "HORN\n" "DOVE\n" "LOCK\n" "HONK\n" "HARP\n" "YARN\n" "DAMP\n" "JAIL\n" "CUSS\n" "WALL\n"
             "MASK\n" "PUNK\n" "MEAT\n" "DISC\n" "HERO\n" "MUSE\n" "MOON\n" "STAR\n" "WORD\n" "SOUL\n" "JINX\n" "EACH\n" "OOZE\n" "COZY\n"
             "ZONE\n" "YETI\n" "YAWN\n" "AXIS\n" "COAX\n" "HAVE\n" "BOXY\n" "QUIT\n" "HAZY\n" "SOIL\n" "LAZY\n"
             "SWAN\n" "SASH\n" "JADE\n" "JOLT\n" "JABS\n" "JUST\n" "ICON\n" "IDOL\n" "INCH\n" "INCH\n" "IDLE\n"
             "IONS\n" "OBOE\n" "OATH\n" "IRON\n" "MINE\n" "KALE\n" "KELP\n" "RASP\n" "RASH\n" "RICH\n" "RING\n" "RIPE\n" "ROBE\n"]

with open('four_letter.txt', 'w',newline='') as f:
    for line in word_list:
        f.write(line)
"""


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
       with open('four_letter.txt') as fh:
        for line in fh:
            word_list.append(line)         
    word = random.choice(word_list)
    wordle(word)
