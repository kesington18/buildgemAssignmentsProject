print("Welcome to Python Pizza Deliveries")

'''size = input("What size pizza do you want? S, M or L: ")


# medium = 20
# large = 25
#
# add_pepperoni_small = 2
# add_pepperoni_medium_or_large = 3
# add_extra_cheese = 1

if size.capitalize() == "S":
    small = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni.capitalize() == "Y":
        small += 2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.capitalize() == "Y":
        small += 1
    print("Your final bill is: ", small)
elif size.capitalize() == "M":
    medium = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni.capitalize() == "Y":
        medium += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.capitalize() == "Y":
        medium += 1
    print("Your final bill is: ", medium)
elif size.capitalize() == "L":
    large = 25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni.capitalize() == "Y":
        large += 2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.capitalize() == "Y":
        large += 1
    print("Your final bill is: ", large)
else:
    print("Sorry, you answer is not within the options provided.")'''

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size.capitalize() == "S":
    bill += 15
elif size.capitalize() == "M":
    bill += 20
elif size.capitalize() == "L":
    bill += 25
else:
    print("Sorry, you answer is not within the options provided.")

if pepperoni.capitalize() == "Y":
    if size.capitalize() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.capitalize() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")