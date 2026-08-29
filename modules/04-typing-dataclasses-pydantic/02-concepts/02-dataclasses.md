# Dataclasses: Typed Data Containers

Dataclasses give you typed records with less boilerplate than regular classes.

## Basic Dataclass

```python
from dataclasses import dataclass

@dataclass
class Order:
    order_id: str
    customer: str
    total: float
    status: str = "pending"  # Default value
```

This auto-generates `__init__`, `__repr__`, and `__eq__`:

```python
order = Order(order_id="ORD-001", customer="Acme", total=150.0)
print(order)  # Order(order_id='ORD-001', customer='Acme', total=150.0, status='pending')
```

## Field Options

```python
from dataclasses import dataclass, field

@dataclass
class Order:
    order_id: str
    items: list[str] = field(default_factory=list)  # Mutable default!
    total: float = 0.0
    tags: set[str] = field(default_factory=set)
```

> Never use `items: list = []` — the same list object is shared across all instances.

## Methods and Properties

```python
@dataclass
class Order:
    order_id: str
    subtotal: float
    tax_rate: float = 0.10

    @property
    def tax(self) -> float:
        return self.subtotal * self.tax_rate

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "subtotal": self.subtotal,
            "tax": self.tax,
            "total": self.total,
        }
```

## Dataclass vs dict

| Feature | `dict` | `dataclass` |
|---------|--------|-------------|
| Typed fields | No | Yes |
| Default values | `.get()` pattern | Field defaults |
| IDE autocomplete | No | Yes |
| Validation | Manual | Can add `__post_init__` |
| Serialization | Built-in | `.to_dict()` |