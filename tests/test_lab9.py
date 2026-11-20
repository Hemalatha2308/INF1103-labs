import unittest
from unittest.mock import Mock, patch
from pathlib import Path
import tempfile

from order import Order
from product import Product
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from order_line import OrderLine
from input_helpers import get_positive_float
from inventory import Inventory
from csv_loader import load_products


class TestDiscountStrategy(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)

    def test_student_discount(self):
        self.assertEqual(StudentDiscount().apply(250), 212.5)

    def test_change_discount(self):
        product = Mock(spec=Product)
        product.get_price.return_value = 125.0

        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(product, 2)

        self.assertEqual(order.calculate_total(), 230)

        order.set_discount(PercentageDiscount(10))

        self.assertEqual(order.calculate_total(), 225)


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@example.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Desk Lamp", 25, 10,
            self.supplier, weight=2.5
        )
        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Photo Editor", 49.90, 100,
            self.supplier, download_size=250
        )
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type"):
            ProductFactory.create(
                "service", "S001", "Installation", 30, 5,
                self.supplier
            )


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@example.com"
        )

    def test_valid_product(self):
        product = PhysicalProduct(
            "P001", "Desk Lamp", 25, 10, 2.5, self.supplier
        )
        self.assertEqual(product.get_name(), "Desk Lamp")

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Chair", 0, 5, 3.0, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P003", "Monitor", 100, -5, 4.0, self.supplier
            )

    def test_negative_stock_update(self):
        product = PhysicalProduct(
            "P004", "Mouse", 15, 10, 0.2, self.supplier
        )
        with self.assertRaises(ValueError):
            product.update_stock(-10)

    def test_invalid_order_quantity(self):
        product = PhysicalProduct(
            "P005", "Keyboard", 30, 5, 0.5, self.supplier
        )
        with self.assertRaises(ValueError):
            OrderLine(product, 0)


class TestInputHandling(unittest.TestCase):

    @patch("builtins.input", side_effect=["abc", "-5", "12.50"])
    @patch("builtins.print")
    def test_invalid_input_then_valid_input(self, mock_print, mock_input):
        result = get_positive_float("Enter price: ")

        self.assertEqual(result, 12.50)
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(mock_print.call_count, 2)


class TestCSVLoading(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@example.com"
        )

    def test_load_valid_and_invalid_rows(self):
        csv_content = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Desk Lamp,25.00,10\n"
            "digital,D001,Photo Editor,49.90,100\n"
            "service,S001,Installation,30.00,5\n"
            "physical,P002,Office Chair,abc,3\n"
            "physical,P003,Monitor Stand,39.50,7\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "products.csv"
            csv_path.write_text(csv_content)

            inventory = Inventory()

            with patch("builtins.print"):
                load_products(
                    str(csv_path), inventory, self.supplier
                )

            self.assertEqual(len(inventory.get_all_products()), 3)

    def test_missing_csv_file(self):
        inventory = Inventory()

        with patch("builtins.print") as mock_print:
            load_products(
                "missing_test_file.csv",
                inventory,
                self.supplier
            )

        messages = [
            str(call) for call in mock_print.call_args_list
        ]

        self.assertTrue(
            any("Products file not found" in message for message in messages)
        )
        self.assertTrue(
            any("Load attempt finished." in message for message in messages)
        )


if __name__ == "__main__":
    unittest.main()