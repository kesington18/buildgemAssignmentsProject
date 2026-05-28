import random
from typing import Any
from art import logo, vs

from game_data import data as game_data

def game_random_comparison(randomA):
    randomB = random.choice(game_data)

    while randomA == randomB:
        randomB = random.choice(game_data)

    return randomB


def game_logic():
    score = 0
    continueGaming = True
    randomA = random.choice(game_data)
    randomB = game_random_comparison(randomA)
    print(logo)

    while continueGaming:
        print(f"Compare A: {randomA["name"]}, a {randomA["description"]}, from {randomA['country']}.")
        print(f"\n {vs} \n")
        print(f"Against B: {randomB["name"]}, a {randomB["description"]}, from {randomB['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ")

        if randomA["follower_count"] > randomB["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"

        if user_input.capitalize() == correct_answer:
            score += 1
            randomA = randomB
            randomB = game_random_comparison(randomA)
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

game_logic()
# print(randomA, randomB)