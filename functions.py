import random

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

word_list = ["apple", "banana", "cherry"]
rnd = random.choice(word_list)

placeholder = ["_"] * len(rnd)
print(rnd)
print("".join(placeholder))
user_lives = 6

while "_" in placeholder and user_lives > 0:
    userInput = input("Guess a letter: ").lower()
    for i in range(0, len(rnd)):
        if userInput == rnd[i]:
            placeholder[i] = rnd[i]
            # print("right")
    if userInput not in rnd:
            user_lives -= 1
            print(f"Letter '{userInput}' is not in the word.")
            # print("wrong")

    print(hangman[user_lives])
    print("".join(placeholder))

if "_" not in placeholder:
    print("You win!")
else:
    print("You lose!")

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