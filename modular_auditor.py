#Initialize inventory auditor
inventory = 0
failed_entries = 0

# Add get_valid_input function to prompt user for stock quantity and invalid input handling
def get_valid_input():
    quantity = ""
    while quantity != "quit":
        quantity = input("Enter stock quantity or 'quit':")

        if quantity == "quit":
            return "quit"

        elif quantity.isdigit():
            return int(quantity)

        else:
            print("Invalid input. Please enter a number.")
    
#add process_delivery function to add the delivery to the total
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total 
