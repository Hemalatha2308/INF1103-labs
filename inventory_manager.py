import json

# Inventory list
inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

def load_inventory():
    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()
        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory
    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")
        return []


inventory = load_inventory()

