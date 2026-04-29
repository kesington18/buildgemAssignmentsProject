import random

word_list = ["apple", "banana", "cherry"]
rnd = random.choice(word_list)

print(rnd)
userInput = input("Guess a letter: ")
for word in rnd:
    if userInput == word:
        print("right")
    else:
        print("wrong")