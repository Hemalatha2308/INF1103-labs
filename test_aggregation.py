from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory


supplier = Supplier("S001", "ABC Supplier", "abc@example.com")

product = PhysicalProduct(
    "P001",
    "Monitor",
    299.90,
    10,
    4.5,
    supplier
)

inventory = Inventory()

inventory.add_product(product)

print("Before removal:")
inventory.display_all()

inventory.remove_product("P001")

print("\nAfter removal:")
inventory.display_all()

print("\nProduct still exists:")
product.display_information()