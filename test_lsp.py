from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "ABC Supplier", "abc@example.com")

physical = PhysicalProduct(
    "P001", "Monitor", 299.90, 10, 4.5, supplier
)

digital = DigitalProduct(
    "D001", "Antivirus", 49.90, 100, 250.0, supplier
)

print("Physical Product:")
show_product_details(physical)

print("\nDigital Product:")
show_product_details(digital)

print("\n========== POLYMORPHISM TEST ==========")

inventory = Inventory()

inventory.add_product(physical)
inventory.add_product(digital)

for product in inventory.get_all_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print("----------------------------------------")