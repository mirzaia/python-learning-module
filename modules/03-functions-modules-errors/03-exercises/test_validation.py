"""Tests for the validation package."""

import pytest
from validation import validate_order_id, validate_total, validate_email, ValidationError


class TestValidateOrderId:
    def test_valid_order_id(self):
        assert validate_order_id("ORD-001") == "ORD-001"

    def test_empty_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_order_id("")
        assert exc.value.field == "order_id"

    def test_invalid_prefix_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_order_id("INVALID")
        assert exc.value.field == "order_id"


class TestValidateTotal:
    def test_positive_total(self):
        assert validate_total(100.0) == 100.0

    def test_zero_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_total(0)
        assert exc.value.field == "total"

    def test_negative_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_total(-50.0)
        assert exc.value.field == "total"


class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") == "user@example.com"

    def test_no_at_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_email("userexample.com")
        assert exc.value.field == "email"

    def test_no_domain_raises(self):
        with pytest.raises(ValidationError) as exc:
            validate_email("user@")
        assert exc.value.field == "email"