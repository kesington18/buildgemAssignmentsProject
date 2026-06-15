from prettytable import PrettyTable as pt

# Master Supermarket Inventory
inventory = {
    1: {"name": "Organic Bananas", "category": "Produce", "price": 0.89, "stock": 150},
    2: {"name": "Honeycrisp Apples", "category": "Produce", "price": 2.49, "stock": 90},
    3: {"name": "Avocados", "category": "Produce", "price": 1.25, "stock": 60},
    4: {"name": "Baby Spinach (1lb)", "category": "Produce", "price": 3.99, "stock": 45},

    5: {"name": "Whole Milk (1 Gal)", "category": "Dairy", "price": 3.69, "stock": 40},
    6: {"name": "Greek Yogurt (32oz)", "category": "Dairy", "price": 4.49, "stock": 35},
    7: {"name": "Unsalted Butter (4 sticks)", "category": "Dairy", "price": 4.19, "stock": 50},
    8: {"name": "Cheddar Cheese Block (8oz)", "category": "Dairy", "price": 2.99, "stock": 55},

    9: {"name": "Sourdough Bread", "category": "Bakery", "price": 4.25, "stock": 20},
    10: {"name": "Whole Wheat Bread", "category": "Bakery", "price": 2.99, "stock": 30},
    11: {"name": "Chocolate Chip Cookies (12ct)", "category": "Bakery", "price": 4.99, "stock": 15},

    12: {"name": "Boneless Chicken Breasts (1lb)", "category": "Meat", "price": 5.99, "stock": 25},
    13: {"name": "Lean Ground Beef 93% (1lb)", "category": "Meat", "price": 6.49, "stock": 20},
    14: {"name": "Fresh Salmon Fillet (1lb)", "category": "Meat", "price": 9.99, "stock": 12},

    15: {"name": "Brown Rice (2lb)", "category": "Pantry", "price": 1.89, "stock": 80},
    16: {"name": "Olive Oil (16.9oz)", "category": "Pantry", "price": 8.99, "stock": 25},
    17: {"name": "Canned Black Beans", "category": "Pantry", "price": 0.99, "stock": 120},
    18: {"name": "Peanut Butter (16oz)", "category": "Pantry", "price": 2.79, "stock": 65},
    19: {"name": "Spaghetti Pasta (1lb)", "category": "Pantry", "price": 1.49, "stock": 100},
    20: {"name": "Marinara Pasta Sauce (24oz)", "category": "Pantry", "price": 3.29, "stock": 70}
}


cart = {}

def resource_check():
    table = pt()
    table.field_names = ["Item ID", "Name", "Category", "Price", "Stock"]

    for key, value in inventory.items():
        table.add_row([key, value["name"], value["category"], f"${value['price']}", value["stock"]])

    return table

def add_to_cart(item_id, amount):
    if item_id in inventory:
        user_item = inventory[item_id]

        if amount > inventory[item_id]["stock"]:
            print(f"Sorry, we only have {user_item['stock']} left in stock.")
            return
        else:
            user_item["stock"] -= amount
            if item_id in cart:
                cart[item_id] += amount
            else:
                cart[item_id] = amount

        print(f"\n✅ Added {amount}x {user_item['name']} to your cart!")
    else:
        print("Sorry, that item is not in the inventory.")


def checkout():
    print("\n--- YOUR FINAL RECEIPT ---")
    receipt_table = pt()
    receipt_table.field_names = ["Item", "Qty", "Unit Price", "Total"]

    price_total = 0
    total_item = 0.0

    for key, value in inventory.items():
        if key in cart:
            price = cart[key] * value["price"]
            price_total += price
            total_item += cart[key]

            receipt_table.add_row([
                value["name"],
                cart[key],
                f"${value['price']}",
                f"${price:.2f}"
            ])

    # Add a visual divider row to separate items from totals
    receipt_table.add_row(["-" * 20, "-" * 5, "-" * 10, "-" * 10])

    # Add the final summary rows at the very bottom
    receipt_table.add_row(["TOTAL", total_item, "", f"${price_total:.2f}"])
    # receipt_table.add_row(["GRAND TOTAL PRICE", "", "", ])

    print(receipt_table)
    # print(f"Grand Total: ${total_item:.2f}")
    print("Thank you for shopping at KENITAM STORES!")


print("Welcome to KENITAM STORES")
print(f"this are our inventory table \n {resource_check()}")

continueShopping = True

while continueShopping:
    user_input = input("\nEnter the ID of the item you want (or type 'checkout' to finish): ").strip().lower()
    if user_input == "checkout":
        checkout()
        continueShopping = False
    elif user_input == "resource":
        print(resource_check())
    elif not user_input.isdigit():
        print("Please enter a valid numeric ID.")
    else:
        userId = int(user_input)

        try:
            user_amount = int(input("Please enter the amount of item you want: "))
            if user_amount <= 0 or not user_amount:
                print("Sorry, Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid numeric ID.")
            continue

        add_to_cart(userId, user_amount)


# table.align = "l"