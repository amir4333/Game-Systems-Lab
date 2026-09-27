# Inventory System

A reusable inventory system built with Python as part of **Game-Systems-Lab**.

The system is designed to manage item data and inventory state independently from game-specific content, UI, and presentation logic.

---

## Architecture

The Inventory System separates item type data from individual item instances and inventory storage:

```text
ItemDefinition
      │
      ├──────────────► ItemInstance
      │
      ▼
InventorySlot
      │
      ▼
Inventory
```

### `ItemDefinition`

Defines the shared properties of an item type.

Current properties:

* `id`
* `name`
* `stackable`
* `max_stack`
* `max_durability`

An `ItemDefinition` describes the type of item rather than a unique physical copy.

### `ItemInstance`

Represents a unique instance of an item when individual identity or state is required.

Current properties:

* `unique_id`
* `item_definition`
* `current_durability`

### `InventorySlot`

Represents an item type and its quantity inside the inventory.

Current properties:

* `item_definition`
* `quantity`

### `Inventory`

Manages the collection of inventory slots.

Current operations include:

* `add_item()`
* `remove_item()`
* `get_slot()`
* `get_slot_with_space()`

---

## Current Features

* Add items to an inventory.
* Remove items from an inventory.
* Stack items up to their maximum stack size.
* Split large quantities across multiple slots.
* Handle non-stackable items as separate slots.
* Remove items across multiple slots.
* Return the actual number of removed items when the requested amount exceeds the available amount.
* Validate zero and negative quantities/counts.
* Keep the core inventory logic independent from UI and game-specific systems.

---

## Item Stacking

Stackable items can share inventory slots up to `max_stack`.

For example, with `max_stack = 10`:

```text
Apple × 10
Apple × 10
Apple × 7
```

Non-stackable items occupy separate slots:

```text
Sword × 1
Sword × 1
Sword × 1
```

---

## Removal Behavior

`remove_item()` can remove items from multiple slots when necessary.

If more items are requested than the inventory contains, the method removes everything available and returns the actual number removed.

Example:

```text
Inventory:
Apple × 10
Apple × 7

Requested: 100
Removed: 17
```

---

## Input Rules

The current inventory contract is:

* `quantity = 0` → no operation; returns `0`.
* `count = 0` → no operation; returns `0`.
* Negative `quantity` → raises `ValueError`.
* Negative `count` → raises `ValueError`.

---

## Demo

`demo.py` provides a console-based demonstration and manual validation of the system.

It covers:

* Basic item addition.
* Filling an existing stack.
* Creating multiple stacks.
* Adding non-stackable items.
* Partial removal.
* Removal across multiple slots.
* Removing more items than are available.
* Removing an item that does not exist.
* Zero and negative input edge cases.

The demo is executed as a package module from the repository root:

```bash
python -m systems.InventorySystem.demo
```

---

## Structure

```text
InventorySystem/
│
├── __init__.py
├── ItemDefinition.py
├── ItemInstance.py
├── InventorySlot.py
├── Inventory.py
├── demo.py
└── README.md
```

---

## Design Goals

The system is intentionally kept independent from presentation and game-specific logic.

The current design aims to be:

* **Reusable** — usable across different games and projects.
* **Independent** — no dependency on UI or a specific game.
* **Understandable** — simple enough to reason about and explain.
* **Extensible** — structured so future inventory features can be added without rewriting the core model.
* **Testable** — behavior can be validated independently through the demo and future automated tests.

The system is deliberately kept small at this stage. More advanced features such as inventory capacity, serialization, equipment integration, and inventory events can be added later if they become necessary.
