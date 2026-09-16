#Initialize inventory auditor
inventory = 0
failed_entries = 0
quantity = ""


# Add while loop to prompt user for stock quantity and invalid input handling
while quantity != "quit":
    quantity = input("Enter stock quantity or 'quit': ")

    if quantity == "quit":
        break

    elif quantity.isdigit():
        quantity = int(quantity)

        if quantity < 0:
            print("Negative numbers are not allowed.")
            failed_entries += 1

        else:
            inventory += quantity

            if inventory > 500:
                print("ALERT: Inventory exceeds 500 units!")
                break

    else:
        print("Invalid input. Please enter a number.")
        failed_entries += 1

# Print the total inventory and number of failed/rejected entries
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)