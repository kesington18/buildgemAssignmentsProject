print("Welcome to Treasure Island")
print("You have been logged in \n Your mission is to find the treasure at Dream Island")

first_movement = input("You are at a cross road. Where do you want to go? \n Type 'left' or 'right' ")


if first_movement.lower() == "left":
    print("congratulations")
    second_movement = input("you made the right choice. \n Welcome, you have gotten to Birth Lake, There is an island in the middle of the lake. \n Do you want to 'swim' across the lake or 'wait' for aerial support? ")
    if second_movement.lower() == "wait":
        print("The royal dragon has descended to carry over to the Dream Island")
        third_movement = input("Welcome to the three doors of Dream Island. Which of the doors do you want to go open? \n Type 'Red' or 'Yellow' or 'Blue' ")
        if third_movement.lower() == "red":
            print("You were burned by the untamed dragons of Dream Island")
        elif third_movement.lower() == "yellow":
            print("Welcome to the treasure of Dream Island, \n YOU WIN")
        else:
            print("You entered the battle arena of monsters. \n Game Over")
    else:
        print("You were attacked by sea monsters lurking beneath the Birth Lake. Game Over")
else:
    print("You fell into a hole, omoooo. Game Over")