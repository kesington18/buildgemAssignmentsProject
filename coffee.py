MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def get_report():
    for key, value in resources.items():
        print(f"{key}: {value}")

def expresso(quart: int, dim: int, nick: int, penn: int):
    total =  0.25 * quart +  0.05 * dim + 0.05 * nick + 0.01 * penn

    if total < MENU["espresso"]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] = total


def start_coffee():
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "espresso":

    elif user_input == "latte":

    elif user_input == "cappuccino":

    elif user_input == "report":
        get_report()

    elif user_input == "off":

    else:
        print("Sorry, Invalid input.")
get_report()