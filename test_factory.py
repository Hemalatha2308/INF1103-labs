from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

physical = ProductFactory.create(
    "physical", "P001", "Desk Lamp", 25.00, 10,
    supplier, weight=2.5
)

digital = ProductFactory.create(
    "digital", "D001", "Photo Editor", 49.90, 100,
    supplier, download_size=250.0
)

print("Physical product:", isinstance(physical, PhysicalProduct))
print("Digital product:", isinstance(digital, DigitalProduct))

try:
    ProductFactory.create(
        "service", "S001", "Installation", 30.00, 5, supplier
    )
except ValueError as error:
    print(error)