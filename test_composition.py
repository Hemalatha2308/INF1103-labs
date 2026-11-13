from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order


supplier = Supplier("S001", "ABC Supplier", "abc@example.com")

monitor = PhysicalProduct(
    "P001", "Monitor", 299.90, 10, 4.5, supplier
)

mouse = PhysicalProduct(
    "P002", "Mouse", 15.00, 20, 0.2, supplier
)

order = Order("O001")

order.add_order_line(monitor, 2)
order.add_order_line(mouse, 3)

print("Order ID:", order.order_id)

print("Order Total: $", f"{order.calculate_total():.2f}")

order2 = Order("O002")
order2.add_order_line(monitor, 1)

print("\nSecond Order ID:", order2.order_id)
print("Second Order Total: $", f"{order2.calculate_total():.2f}")

print("\nAre the OrderLine objects the same?")
print(order.order_lines[0] is order2.order_lines[0])

print("\nAre the Product objects the same?")
print(order.order_lines[0].product is order2.order_lines[0].product)