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

#add calculate_tax function to calculate 10% tax on the total amount
def calculate_tax(amount):
    tax = amount * 0.10
    return tax

#add generate_report function to display the total units processed and number of failed/rejected entries
def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

