import random
from data.word_generator import WordClass
import string
from termcolor import colored
import inquirer

GAME_LEVEL = [
    inquirer.List('level',
                    message="Please select game level : Maximum Lives are Easiest => 25, Easy => 10, Normal => 7, Hard => 3, Nightmare => 1",
                    choices=['Easiest', 'Easy', 'Normal', 'Hard', 'Nightmare'],
                    default='Normal'
    ),
]

CONTINUE_GAME = [
    inquirer.List('continue',
                    message="\nGuess another word ??", 
                    choices=['Yayyyy', 'Nahhh I am done for now'],
                    default='Yayyyy'  
    ),
]

class HangMan:

    # Game level helps us tweek the words and no of guesses
    # The level contains MinWordLength, Maximum WordLength, Maximum corpus count, Maximum guesses possible

    GAME_LEVEL_MAPPING = {
    "Easiest" : [6, 8, 15, 25],
    "Easy" : [5, 10, 10, 10],
    "Normal" : [5, 13, 7, 7],
    "Hard" : [10, 24, 5, 3],
    "Nightmare" : [15, 24, 2, 1],
    }

    def valid(word):
        w = random.choice(word)
        while '-' in word or ' ' in word:
            w= random.choice(word)

        return w.upper()

    def headerPrinter(lives, used_char):
        msg_lives = colored("Lives left : ", 'green')
        msg_lives_count = colored(lives, "green", attrs=['bold']) 
        msg_used_char = colored(" Letters used : [ ", "green")
        msg_used_char_count = colored(" ".join(used_char), "green", attrs=['bold'])
        msg_end = colored(" ]", "green", attrs=['bold'])
        print(f"\n\t\t{msg_lives} {msg_lives_count} **** {msg_used_char} {msg_used_char_count}{msg_end}")
    
    def gameOverPrinter(word):
        msg = colored("[!!!] GAME OVER. ", "red", attrs=['bold'])
        mid_msg = colored("The word was", 'red')
        word_answer = colored(word, "magenta", attrs=['bold'])
        print(f"\n\t\t{msg} {mid_msg} :  {word_answer}")

    def gameWonPrinter(word):
        msg = colored("Woohooo - You Won!!! ", "green", attrs=['bold'])
        mid_msg = colored(" Correct Word", 'green')
        word_answer = colored(word, "magenta", attrs=['bold'])
        print(f"\n\t{msg} {mid_msg} :  {word_answer}")

    def decrement_lives(lives):
        return lives - 1


    def hangman(game_level):
        #TODO change to upper
        word = WordClass.getRandomWordFromList(game_level[0], game_level[1], game_level[2])
        word_letter =  set(word.upper())
        alphabet = set(string.ascii_uppercase)
        used_char = set() # empty for now

        lives = game_level[3]
        # Loop until end of lives or winning the game
        while len(word_letter)>0 and lives>0:
            HangMan.headerPrinter(lives, used_char)
            
            # current status of word with char if already found or _ if not found 
            currentCondition = []
            for character in word.upper():
                if character in used_char:
                    currentCondition.append(character)
                else:
                    currentCondition.append("_")
            current_word = colored(" ".join(currentCondition), 'cyan', attrs=['bold'])
            print(f"\t\tCurrent Condition: {current_word}")

            # Getting input from user
            user_letter = input('\t\tGuess a letter now => ').upper()

            if user_letter in alphabet - used_char:
                # Add character to used char array
                used_char.add(user_letter)
            
                if user_letter in  word_letter:
                    # input letter a valid guess
                    word_letter.remove(user_letter)
                else:
                    # input letter is wrong guess, decrement lives
                    lives = HangMan.decrement_lives(lives)
            elif user_letter in used_char:
                # Input character is alrady used
                print(colored("\t\t[!!!] Already used, try a new character", "red"))
                lives = HangMan.decrement_lives(lives)
            
            else:
                # Input letter is an invalid character
                print(colored("\t\t[!!!] Invalid character\t\t", "red"))
                lives = HangMan.decrement_lives(lives)

        if lives == 0:
            HangMan.gameOverPrinter(word)
        else:
            HangMan.gameWonPrinter(word)

if __name__ == "__main__":

    print(colored("#" * 122, "cyan", attrs=['bold']))
    var = "#" * 50
    welcome_msg = var + "\tHANGMAN!\t" + var
    print(colored(welcome_msg, "cyan", attrs=['bold']))
    print(colored("#" * 122, "cyan", attrs=['bold']))
    # print("\n\{intro_line} {msg_lives_count} ----- {msg_used_char} {msg_used_char_count}")

    continue_playing_flag = True

    while continue_playing_flag:
        answers = inquirer.prompt(GAME_LEVEL)
        game_level = HangMan.GAME_LEVEL_MAPPING.get(answers["level"])

        HangMan.hangman(game_level)

        answer = inquirer.prompt(CONTINUE_GAME)['continue']
        if answer == "Nahhh I am done for now":
            continue_playing_flag = False