
from supplier import Supplier
from physical_product import PhysicalProduct
from order_line import OrderLine

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

# Valid product
product = PhysicalProduct(
    "P001", "Desk Lamp", 25.00, 10, 2.5, supplier
)

print("Valid product created:", product.get_name())

# Invalid product price
try:
    PhysicalProduct("P002", "Chair", 0, 5, 3.0, supplier)
except ValueError as error:
    print(error)

# Invalid product stock
try:
    PhysicalProduct("P003", "Monitor", 100, -5, 4.0, supplier)
except ValueError as error:
    print(error)

# Invalid stock update
try:
    product.update_stock(-10)
except ValueError as error:
    print(error)

# Invalid order quantity
try:
    OrderLine(product, 0)
except ValueError as error:
    print(error)
