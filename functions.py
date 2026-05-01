import random

words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

hangman = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

rnd = random.choice(words)

placeholder = ["_"] * len(rnd)
# print(rnd)
user_lives = 6
print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
print(f'Word to guess: {"".join(placeholder)}')
while "_" in placeholder and user_lives > 0:

    print(f"*******************************{user_lives}/6 LIVES LEFT************************************")
    userInput = input("Guess a letter: ").lower()

    if userInput in placeholder:
        user_lives -= 1
        print(f"You have guessed the letter '{userInput}'. You have {user_lives} LIVES LEFT")
    elif userInput not in rnd:
        user_lives -= 1
        print(f"Letter '{userInput}' is not in the word.")
        # print("wrong")
    else:
        for i in range(0, len(rnd)):
            if userInput == rnd[i]:
                placeholder[i] = rnd[i]
                # print("right")


    print(hangman[user_lives])
    print("".join(placeholder))

if "_" not in placeholder:
    print("You win!")
else:
    print(f"You lose! The answer is {rnd}")

'''another Solution by angela yu'''
'''game_over = False
correct_letters = []

while not game_over:
    userInput = input("Guess a letter: ").lower()

    display = ""

    for letter in rnd:
        if userInput == letter:
            display += letter
            correct_letters.append(userInput)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over = True
        print("you win!")'''