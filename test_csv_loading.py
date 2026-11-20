from inventory import Inventory
from supplier import Supplier
from csv_loader import load_products


# Create an empty inventory
inventory = Inventory()

# Create a supplier
supplier = Supplier(
    "S001",
    "Default Supplier",
    "default@example.com"
)

# Load products from CSV
load_products("products.csv", inventory, supplier)

# Display the loaded products
print("\nProducts in inventory:")
inventory.display_all()

# Display the number of products loaded
print("Total products:", len(inventory.get_all_products()))


# Test missing CSV file
print("\nTesting missing CSV file:")
load_products("missing.csv", Inventory(), supplier)