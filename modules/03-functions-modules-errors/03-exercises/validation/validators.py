"""Validation functions for order processing."""

from validation.errors import ValidationError


def validate_order_id(order_id: str) -> str:
    """Validate that order_id is non-empty and starts with 'ORD-'.

    Args:
        order_id: The order identifier string.

    Returns:
        The validated order_id.

    Raises:
        ValidationError: If order_id is empty or doesn't start with 'ORD-'.
    """
    # TODO: Implement validation
    pass


def validate_total(total: float) -> float:
    """Validate that total is positive.

    Args:
        total: The order total amount.

    Returns:
        The validated total.

    Raises:
        ValidationError: If total is zero or negative.
    """
    # TODO: Implement validation
    pass


def validate_email(email: str) -> str:
    """Validate that email contains '@' and has a domain part.

    Args:
        email: The email address to validate.

    Returns:
        The validated email.

    Raises:
        ValidationError: If email doesn't contain '@' or has no domain.
    """
    # TODO: Implement validation
    pass