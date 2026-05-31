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


def coffee_make(quart: int, dim: int, nick: int, penn: int, coffee: str):
    total = 0.25 * quart + 0.05 * dim + 0.05 * nick + 0.01 * penn

    change = round(total - MENU[coffee]["cost"], 2)

    if total < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if "money" not in resources:
            resources["money"] = MENU[coffee]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee} ☕️. Enjoy!")

        else:
            resources["money"] += MENU[coffee]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee} ☕️. Enjoy!")


def coffee_question():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    return quarters, dimes, nickles, pennies

def start_coffee():
    continueMaking = True

    while continueMaking:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # 1. Safely grab the ingredients dictionary (fallback to empty dict if drink doesn't exist)
        ingredients = MENU.get(user_input.lower(), {}).get("ingredients", {})

        # 2. Extract each ingredient. If it doesn't exist (like milk in espresso), default to 0!
        water = ingredients.get("water", 0)
        milk = ingredients.get("milk", 0)
        coffee = ingredients.get("coffee", 0)

        if resources["water"] < water:
            print("Sorry there is not enough water.")
            continue
        elif resources["milk"] < milk:
            print("Sorry there is not enough milk.")
            continue
        elif resources["coffee"] < coffee:
            print("Sorry there is not enough coffee.")
            continue
        else:
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee

        if user_input == "espresso":
            quarters, dimes, nickles, pennies = coffee_question()
            coffee_make(quarters, dimes, nickles, pennies, user_input)

        elif user_input == "latte":
            quarters, dimes, nickles, pennies = coffee_question()
            coffee_make(quarters, dimes, nickles, pennies, user_input)

        elif user_input == "cappuccino":
            quarters, dimes, nickles, pennies = coffee_question()
            coffee_make(quarters, dimes, nickles, pennies, user_input)

        elif user_input == "report":
            get_report()

        elif user_input == "off":
            continueMaking = False
        else:
            print("Sorry, Invalid input.")

start_coffee()