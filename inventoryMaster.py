# Master Supermarket Inventory
inventory = {
    101: {"name": "Organic Bananas", "category": "Produce", "price": 0.89, "stock": 150},
    102: {"name": "Honeycrisp Apples", "category": "Produce", "price": 2.49, "stock": 90},
    103: {"name": "Avocados", "category": "Produce", "price": 1.25, "stock": 60},
    104: {"name": "Baby Spinach (1lb)", "category": "Produce", "price": 3.99, "stock": 45},

    105: {"name": "Whole Milk (1 Gal)", "category": "Dairy", "price": 3.69, "stock": 40},
    106: {"name": "Greek Yogurt (32oz)", "category": "Dairy", "price": 4.49, "stock": 35},
    107: {"name": "Unsalted Butter (4 sticks)", "category": "Dairy", "price": 4.19, "stock": 50},
    108: {"name": "Cheddar Cheese Block (8oz)", "category": "Dairy", "price": 2.99, "stock": 55},

    109: {"name": "Sourdough Bread", "category": "Bakery", "price": 4.25, "stock": 20},
    110: {"name": "Whole Wheat Bread", "category": "Bakery", "price": 2.99, "stock": 30},
    111: {"name": "Chocolate Chip Cookies (12ct)", "category": "Bakery", "price": 4.99, "stock": 15},

    112: {"name": "Boneless Chicken Breasts (1lb)", "category": "Meat", "price": 5.99, "stock": 25},
    113: {"name": "Lean Ground Beef 93% (1lb)", "category": "Meat", "price": 6.49, "stock": 20},
    114: {"name": "Fresh Salmon Fillet (1lb)", "category": "Meat", "price": 9.99, "stock": 12},

    115: {"name": "Brown Rice (2lb)", "category": "Pantry", "price": 1.89, "stock": 80},
    116: {"name": "Olive Oil (16.9oz)", "category": "Pantry", "price": 8.99, "stock": 25},
    117: {"name": "Canned Black Beans", "category": "Pantry", "price": 0.99, "stock": 120},
    118: {"name": "Peanut Butter (16oz)", "category": "Pantry", "price": 2.79, "stock": 65},
    119: {"name": "Spaghetti Pasta (1lb)", "category": "Pantry", "price": 1.49, "stock": 100},
    120: {"name": "Marinara Pasta Sauce (24oz)", "category": "Pantry", "price": 3.29, "stock": 70}
}

li = []
for key, value in inventory.items():
    li.append(value["category"].lower())
    print(key)
# print(set(li))

user_input = input("Please enter your choice of category: 'Produce', 'Dairy', 'Pantry', 'Meat', 'Bakery' ").strip().lower()
if user_input in li:
    for key, value in inventory.items():
        if value["category"].lower() == user_input:
            print(f"{value["name"]} -> ${value["price"]}")
