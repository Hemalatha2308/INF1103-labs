from unittest.mock import patch
from input_helpers import get_positive_float

with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
    result = get_positive_float("Enter price: ")

print("Final price:", result)
