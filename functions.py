import random

word_list = ["apple", "banana", "cherry"]
rnd = random.choice(word_list)

placeholder = ["_"] * len(rnd)
print(rnd)
userInput = input("Guess a letter: ").lower()
for i in range(0, len(rnd)):
    if userInput == rnd[i]:
        placeholder[i] = rnd[i]
        print("right")
    else:
        print("wrong")
print("".join(placeholder))

'''another Solution by angela yu'''
display = ""
for i in range(0, len(rnd)):
    if userInput == rnd[i]:
        display += rnd[i]
        print("right")
    else:
        display += "_"
        print("wrong")
print(display)