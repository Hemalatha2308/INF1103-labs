from product import Product
from inventory import Inventory


inventory = Inventory()

product1 = Product("P001", "Laptop", 1200.00, 15)
product2 = Product("P002", "Mouse", 25.50, 40)
product3 = Product("P003", "Keyboard", 45.00, 25)

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)


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

        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        product = Product(product_id, name, price, stock)
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
        else:
            print("Product not found.")

    elif option == "5":
        print("Save functionality will be added in Phase 4.")

    elif option == "6":
        print("Thank you for using Inventory Management System.")
        break

    else:
        print("Invalid option.")
