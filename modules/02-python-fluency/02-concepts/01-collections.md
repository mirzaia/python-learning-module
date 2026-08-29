# Collections: Lists, Dicts, Sets, Tuples

Python's four core collection types each serve a different purpose. Choosing the right one makes your code clearer and more efficient.

## Lists `[]`

Ordered, mutable, allows duplicates. Use for ordered sequences.

```python
order_ids = ["ORD-001", "ORD-002", "ORD-003"]
order_ids.append("ORD-004")     # mutable
print(order_ids[0])             # "ORD-001" — indexed access
print(order_ids[-1])            # "ORD-004" — negative indexing
print(order_ids[1:3])           # ["ORD-002", "ORD-003"] — slicing
```

## Dicts `{}`

Key-value pairs. Unordered (ordered by insertion in 3.7+), mutable. Use for lookups and structured data.

```python
order = {
    "order_id": "ORD-001",
    "status": "shipped",
    "items": [{"sku": "A1", "qty": 2}],
}
print(order["status"])          # "shipped"
print(order.get("customer", "unknown"))  # "unknown" — safe lookup
```

## Sets `{}` (but `set()` for empty)

Unordered, mutable, unique elements. Use for deduplication and membership.

```python
tags = {"python", "backend", "api"}
tags.add("python")              # no-op — already present
print("api" in tags)            # True — O(1) membership
print(set([1, 2, 2, 3]))        # {1, 2, 3} — deduplication
```

## Tuples `()`

Ordered, immutable, allows duplicates. Use for fixed collections and record types.

```python
point = (10.5, -3.2)
x, y = point                    # unpacking
print(x, y)                     # 10.5 -3.2
```

## When to Use What

| Type | Use when... |
|------|------------|
| `list` | Order matters, you need to add/remove items |
| `dict` | You need key-based lookup, structured data |
| `set` | You need uniqueness, fast membership testing |
| `tuple` | You have a fixed group of values, return multiple values |
