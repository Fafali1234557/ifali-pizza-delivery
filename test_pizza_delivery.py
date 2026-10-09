"""Tests for Ifali's Pizza Delivery price calculations."""

import unittest
from unittest.mock import patch

from pizza_delivery import calculate_total, get_valid_choice


class TestPizzaPricing(unittest.TestCase):
    def test_all_size_and_topping_combinations(self):
        base_prices = {"S": 15, "M": 20, "L": 25}
        pepperoni_prices = {"S": 2, "M": 3, "L": 3}

        for size in base_prices:
            for pepperoni in (False, True):
                for cheese in (False, True):
                    with self.subTest(size=size, pepperoni=pepperoni, cheese=cheese):
                        expected = (
                            base_prices[size]
                            + (pepperoni_prices[size] if pepperoni else 0)
                            + (1 if cheese else 0)
                        )
                        self.assertEqual(calculate_total(size, pepperoni, cheese), expected)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            calculate_total("XL", False, False)

    def test_lowercase_and_whitespace_are_accepted(self):
        with patch("builtins.input", return_value="  m  "):
            self.assertEqual(get_valid_choice("Size: ", ("S", "M", "L")), "M")

    def test_invalid_selection_prompts_again(self):
        with patch("builtins.input", side_effect=["maybe", " n "]):
            with patch("builtins.print") as printed:
                answer = get_valid_choice("Extra cheese? ", ("Y", "N"))
        self.assertEqual(answer, "N")
        printed.assert_called_once()


if __name__ == "__main__":
    unittest.main()
