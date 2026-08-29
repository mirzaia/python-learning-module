"""Custom exceptions for the validation package."""


class ValidationError(Exception):
    """Raised when validation fails.

    Attributes:
        message: Human-readable error description.
        field: The name of the field that failed validation.
    """
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field