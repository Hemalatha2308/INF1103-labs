import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier


def load_inventory():
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        file = open("inventory.json", "r")
        products = json.load(file)
        file.close()

        for item in products:

            if "supplier" in item:
                supplier_data = item["supplier"]

                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

            else:
                supplier = Supplier(
                    "S001",
                    "Default Supplier",
                    "default@example.com"
                )

            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"],
                    supplier
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"],
                    supplier
                )

            else:
                print("Unknown product type:", item["type"])
                continue

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found. Starting with empty inventory.")

    return inventory


def save_inventory(inventory):
    products = []

    for product in inventory.get_all_products():
        item = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
            "supplier": {
                "supplier_id": product.supplier.supplier_id,
                "name": product.supplier.name,
                "contact_email": product.supplier.contact_email
            }
        }

        if isinstance(product, PhysicalProduct):
            item["type"] = "physical"
            item["weight"] = product.get_weight()

        elif isinstance(product, DigitalProduct):
            item["type"] = "digital"
            item["download_size"] = product.get_download_size()

        products.append(item)

    file = open("inventory.json", "w")
    json.dump(products, file, indent=4)
    file.close()

    print("Inventory saved successfully to inventory.json.")


inventory = load_inventory()


while True:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("Add New Product")
        print("1. Physical Product")
        print("2. Digital Product")

        product_type = input("Choose product type: ")

        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        print("Supplier Details")
        supplier_id = input("Supplier ID: ")
        supplier_name = input("Supplier Name: ")
        contact_email = input("Supplier Contact Email: ")

        supplier = Supplier(
            supplier_id,
            supplier_name,
            contact_email
        )

        if product_type == "1":
            weight = float(input("Weight (kg): "))

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                weight,
                supplier
            )

        elif product_type == "2":
            download_size = float(input("Download Size (MB): "))

            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                download_size,
                supplier
            )

        else:
            print("Invalid product type.")
            continue

        inventory.add_product(product)

        print("Product added successfully!")

    elif option == "3":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)
            print("Stock updated successfully!")
        else:
            print("Product not found.")

    elif option == "4":
        product_id = input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, PhysicalProduct):
                print(
                    "Shipping Cost: $",
                    f"{product.calculate_shipping_cost():.2f}"
                )

        else:
            print("Product not found.")

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option.")