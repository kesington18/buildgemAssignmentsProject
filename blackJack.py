import random

continueGaming = True

while continueGaming:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    userResult = 0
    comResult = 0
    comCard = []
    userCard = []

    userInput = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if userInput.lower() == 'y':

        # player starting cards
        for i in range(2):
            userRndCard = random.choice(cards)
            userCard.append(userRndCard)
            userResult += userRndCard

        # computer starting card
        comRndCard = random.choice(cards)
        comCard.append(comRndCard)
        comResult += comRndCard

        print(f"Your cards: {userCard}, current score: {userResult}")
        print(f"Computer's first card: {comRndCard}")

        # player turn
        while userResult <= 21:
            userInput2 = input("Type 'y' to get another card, type 'n' to pass: ")
            if userInput2.lower() == 'y':
                newUserRndCard = random.choice(cards)
                userCard.append(newUserRndCard)
                userResult += newUserRndCard

                # converting the 11 ace to a 1 ace whenever the result id greater than 21 and it includes an 11
                if userResult > 21 and 11 in userCard:
                    userCard.remove(11)
                    userResult -= 10
                    userCard.append(1)

                print(f"Your cards: {userCard}, current score: {userResult}")
                print(f"Computer's first card: {comRndCard}")

                # player bust check
                if userResult > 21:
                    print(f"Your final hand: {userCard}, final score: {userResult}")
                    print(f"Computer's final hand: {comCard}, final score: {comResult}")
                    print("You went over. You lose 😭")
                    break
            elif userInput2.lower() == 'n':

                # computer turn
                while comResult < 17:
                    newComRndCard = random.choice(cards)
                    comCard.append(newComRndCard)
                    comResult += newComRndCard

                # converting the 11 ace to a 1 ace whenever the result id greater than 21 and it includes an 11
                if comResult > 21 and 11 in comCard:
                    comCard.remove(11)
                    comResult -= 10
                    comCard.append(1)

                print(f"Your final hand: {userCard}, final score: {userResult}")
                print(f"Computer's final hand: {comCard}, final score: {comResult}")

                # result checking
                if comResult > 21:
                    print("Opponent went over. You win 😁")
                elif userResult > comResult:
                    print("You win 😁")
                elif comResult > userResult:
                    print("You lose  😭")
                else:
                    print("It's a draw 🙃")
                break


    elif userInput.lower() == 'n':
        continueGaming = False
    else:
        print("Type 'y' or 'n'")
    # print(userCard, comCard, userResult)