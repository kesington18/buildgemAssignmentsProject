import random

continueGaming = True

while continueGaming:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    userInput = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    userResult = 0
    comResult = 0
    comCard = []
    userCard = []

    if userInput.lower() == 'y':
        for i in range(2):
            userRndCard = random.choice(cards)
            userCard.append(userRndCard)
            userResult += userRndCard

        print(f"Your cards: {userCard}, current score: {userResult}")
        comRndCard = random.choice(cards)
        comCard.append(comRndCard)
        comResult += comRndCard
        print(f"Computer's first card: {comRndCard}")

        while userResult <= 21:
            userInput2 = input("Type 'y' to get another card, type 'n' to pass: ")
            if userInput2.lower() == 'y':
                newUserRndCard = random.choice(cards)
                userCard.append(newUserRndCard)
                userResult += newUserRndCard
                print(f"Your cards: {userCard}, current score: {userResult}")
                print(f"Computer's first card: {comRndCard}")
            else:
                print(f"Your final hand: {userCard}, final score: {userResult}")
                while comResult < 17:
                    newComRndCard = random.choice(cards)
                    comCard.append(newComRndCard)
                    comResult += newComRndCard
                print(f"Computer's final hand: {comCard}, final score: {comResult}")

        if userResult > 21 and comResult < 21:
            print(f"You went over. You lose 😭")
        elif userResult < 21 and comResult > 21:
            print(f"Opponent went over. You win 😁")

    continueGaming = False

    print(userCard, comCard, userResult)