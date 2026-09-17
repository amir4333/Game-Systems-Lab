# Inventory System

A reusable inventory system built with Python.

This system is responsible for storing and managing items independently from the game's presentation layer.

---

## Goal

The goal of this system is to provide a simple and reusable foundation for managing items in a game.

It is also used as a foundation for exploring concepts such as item representation, inventory slots, item quantities, and future inventory architecture.

---

## Current Features

* Add items to an inventory.
* Remove items from an inventory.
* Find an item's inventory slot.
* Store item quantities.
* Represent items independently from the inventory itself.
* Store item stacking properties.

---

## Core Classes

### `Item`

Represents an item that can exist in the inventory.

Current properties include:

* `name`
* `stackable`
* `maxStack`

---

### `InventorySlot`

Represents an item and its current quantity inside the inventory.

Each slot contains:

* An `Item`
* A quantity

---

### `Inventory`

Manages the collection of inventory slots.

Current operations include:

* `add_item()`
* `remove_item()`
* `get_slot()`

---

## Structure

```text
InventorySystem/
│
├── Inventory.py
├── InventorySlot.py
├── Item.py
├── demo.py
└── README.md
```

---

## Basic Flow

```text
Item
  │
  ▼
Inventory
  │
  ▼
InventorySlot
  │
  └── Quantity
```

For example:

```text
Inventory

├── Sword × 1
└── Apple × 3
```

---

## Example

A simple inventory can be created and used like this:

```python
sword = Item("Sword")
apple = Item("Apple")

inventory = Inventory()

inventory.add_item(sword)
inventory.add_item(apple, 3)

inventory.remove_item(sword)
```

---

## Current Limitations

This is the first version of the Inventory System and intentionally keeps the architecture simple.

Some concepts are currently represented but not fully enforced by the inventory logic, such as:

* Maximum stack size
* Non-stackable item behavior
* Inventory capacity
* More precise item identity
* Detailed operation results and error handling

These are candidates for future versions.

---

## Planned Improvements

Possible future improvements include:

* Proper stack size enforcement
* Non-stackable item handling
* Inventory capacity
* More robust item identity
* Better operation results
* Item type definitions
* Serialization and save/load support
* Inventory events
* Improved testing
* Better separation between item definitions and item instances

---

## Design Goals

The Inventory System should eventually remain:

* Reusable
* Independent from UI
* Independent from a specific game
* Easy to extend
* Easy to test
* Clear enough to reuse in future projects

---

## Development Status

**Current version: V1**

The basic inventory functionality is implemented.

The next major development stage will focus on reviewing the architecture and improving the system based on its use inside the Game Systems Lab integration demo.
