"""Module 5 exercises: Test the OrderService with edge cases.

Complete the test stubs below. Run with:
    uv run pytest 03-exercises/ -v
"""

import pytest
import sys
sys.path.insert(0, "02-concepts")
from order_service import OrderService


# ---- Exercise 1: Edge Case Tests ----

class TestEmptyOrder:
    def test_calculate_total_returns_zero(self):
        """Empty order should have total of 0."""
        # TODO: create service, assert total == 0
        pass

    def test_is_empty_returns_true(self):
        """Empty order should report is_empty == True."""
        # TODO: create service, assert is_empty is True
        pass


class TestDiscountEdgeCases:
    def test_100_percent_discount(self):
        """100% discount should give 0."""
        # TODO: create service, call apply_discount(100, 100), assert == 0
        pass

    def test_negative_discount_raises(self):
        """Negative discount should raise ValueError."""
        # TODO: create service, assert apply_discount raises ValueError
        pass

    def test_discount_over_100_raises(self):
        """Discount over 100 should raise ValueError."""
        # TODO: create service, assert apply_discount raises ValueError
        pass


class TestValidationErrors:
    def test_zero_quantity_raises(self):
        """Adding an item with quantity 0 should raise ValueError."""
        # TODO: create service, add item with quantity=0, assert raises
        pass

    def test_negative_price_raises(self):
        """Adding an item with negative price should raise ValueError."""
        # TODO: create service, add item with negative price, assert raises
        pass


# ---- Exercise 2: Parametrize ----

# TODO: Add @pytest.mark.parametrize with test cases for apply_discount
def test_apply_discount_parametrized():
    pass


# ---- Exercise 3: Fixture ----

# TODO: Create a fixture that returns a service with 3 pre-added items
# @pytest.fixture
# def populated_service():
#     ...

# TODO: Write a test that uses the fixture to check final_total with 20% discount
# def test_final_total_with_discount(populated_service):
#     ...