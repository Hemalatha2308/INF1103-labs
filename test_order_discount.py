from unittest.mock import Mock
from product import Product
from order import Order
from discount_strategy import PercentageDiscount, BulkDiscount

# Create a mock product with a price of $100
product = Mock(spec=Product)
product.get_price.return_value = 100.0

# Create an order with 2 products
order = Order("O001")
order.add_order_line(product, 2)

# Test default discount
print("Default total:", order.calculate_total())

# Apply 10% discount
order.set_discount(PercentageDiscount(10))
print("After 10% discount:", order.calculate_total())

# Change to bulk discount
order.set_discount(BulkDiscount(200, 20))
print("After bulk discount:", order.calculate_total())