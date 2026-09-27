from ItemDefinition import ItemDefinition
from Inventory import Inventory


def print_inventory(inventory):
    print("\nInventory:")
    for index, slot in enumerate(inventory.slots):
        print(
            f"  Slot {index}: "
            f"{slot.item_definition.name} x{slot.quantity}"
        )


apple = ItemDefinition(
    id="apple",
    name="Apple",
    stackable=True,
    max_stack=10
)

sword = ItemDefinition(
    id="sword",
    name="Sword",
    stackable=False,
    max_stack=1
)

inventory = Inventory()


print("=== ADD TESTS ===")

inventory.add_item(apple, 3)
print_inventory(inventory)

inventory.add_item(apple, 7)
print_inventory(inventory)

inventory.add_item(apple, 12)
print_inventory(inventory)

inventory.add_item(apple, 25)
print_inventory(inventory)

inventory.add_item(sword)
print_inventory(inventory)

inventory.add_item(sword, 5)
print_inventory(inventory)


print("\n=== REMOVE TESTS ===")

removed = inventory.remove_item(apple, 5)
print(f"Requested: 5 | Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(apple, 10)
print(f"Requested: 10 | Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(apple, 100)
print(f"Requested: 100 | Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(apple, 1)
print(f"Requested: 1 | Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(sword)
print(f"Requested: 1 | Removed: {removed}")
print_inventory(inventory)
