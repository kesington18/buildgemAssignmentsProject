import random

logo = r"""
                                                                             ,----,                                                                                                     
                                                                         ,/   .`|                                      ,--.                                                           
  ,----..                                                              ,`   .'  :  ,---,                             ,--.'|                       ____                                
 /   /   \                                                           ;    ;     /,--.' |                         ,--,:  : |                     ,'  , `.  ,---,                       
|   :     :          ,--,                                          .'___,/    ,' |  |  :                      ,`--.'`|  ' :         ,--,     ,-+-,.' _ |,---.'|               __  ,-. 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.           |    :     |  :  :  :                      |   :  :  | |       ,'_ /|  ,-+-. ;   , |||   | :             ,' ,'/ /| 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '          ;    |.';  ;  :  |  |,--.   ,---.          :   |   \ | :  .--. |  | : ,--.'|'   |  ||:   : :      ,---.  '  | |' | 
;   | ;  __ ,'_ /| :  . |   /     \ |  :  /`./ |  :  /`./          `----'  |  |  |  :  '   |  /     \         |   : '  '; |,'_ /| :  . ||   |  ,', |  |,:     |,-.  /     \ |  |   ,' 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_                '   :  ;  |  |   /' : /    /  |        '   ' ;.    ;|  ' | |  . .|   | /  | |--' |   : '  | /    /  |'  :  /   
.   | '_.' :|  | ' |  | | .    ' / | \  \    `. \  \    `.             |   |  '  '  :  | | |.    ' / |        |   | | \   ||  | ' |  | ||   : |  | ,    |   |  / :.    ' / ||  | '    
'   ; : \  |:  | : ;  ; | '   ;   /|  `----.   \ `----.   \            '   :  |  |  |  ' | :'   ;   /|        '   : |  ; .':  | : ;  ; ||   : |  |/     '   : |: |'   ;   /|;  : |    
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /            ;   |.'   |  :  :_:,''   |  / |        |   | '`--'  '  :  `--'   \   | |`-'      |   | '/ :'   |  / ||  , ;    
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /             '---'     |  | ,'    |   :    |        '   : |      :  ,      .-./   ;/          |   :    ||   :    | ---'     
 \   \ .'    `--`----'     \   \  /   `--'---'   `--'---'                        `--''       \   \  /         ;   |.'       `--`----'   '---'           /    \  /  \   \  /           
  `---`                     `----'                                                            `----'          '---'                                     `-'----'    `----'            

"""


def random_number() -> int:
    # Generates a number between 1 and 100 (inclusive)
    return random.randint(1, 100)

def game_logic(attempts: int):
    randomNumber = random_number()

    while attempts > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > randomNumber:
            attempts -= 1
            print(f"Too high. \nGuess again. \nYou have {attempts} attempts remaining to guess the number.")
        elif user_guess < randomNumber:
            attempts -= 1
            print(f"Too low. \n Guess again. \n You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {randomNumber}.")
            return
    print("You've run out of guesses. Refresh the page to run again.")

def check_user_answer():
    attempts = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_input == "easy":
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number.")
        game_logic(attempts)
    elif user_input == "hard":
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number.")
        game_logic(attempts)
    else:
        print("Invalid input. Try again.")

check_user_answer()