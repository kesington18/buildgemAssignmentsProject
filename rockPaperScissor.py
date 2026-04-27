import random

# names = ["alice", "james", "samuel", "samson"]
# print(names[random.randint(0, len(names) - 1)])
# print(random.choice(names))

rps = ["rock", "paper", "scissors"]
rnd = random.randint(0, len(rps)-1)

userInput =  int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
if userInput == 0 and rnd == 1:
    print(f"computer won! you chose {rps[userInput]} and computer chose {rps[rnd]}")
elif userInput == 1 and rnd == 2:
    print(f"computer won! you chose {rps[userInput]} and computer chose {rps[rnd]}")
elif userInput == 2 and rnd == 0:
    print(f"computer won! you chose {rps[userInput]} and computer chose {rps[rnd]}")
elif userInput == rnd:
    print(f"It is a draw you picked {rps[userInput]} and computer chose {rps[rnd]}")
elif userInput >= 3 or userInput < 0:
    print(f"you typed an incorrect input. Try again")
else:
    print(f"You won! you chose {rps[userInput]} and computer chose {rps[rnd]}")
