from ItemDefinition import ItemDefinition
from Inventory import Inventory


def print_inventory(inventory):
    print("Inventory:")
    for index, slot in enumerate(inventory.slots):
        print(
            f"  Slot {index}: "
            f"{slot.item_definition.name} x{slot.quantity}"
        )
    print()


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

print("=== Add Items ===")

inventory.add_item(apple, 3)
print_inventory(inventory)

inventory.add_item(apple, 7)
print_inventory(inventory)

inventory.add_item(apple, 12)
print_inventory(inventory)

inventory.add_item(sword, 1)
print_inventory(inventory)


print("=== Remove Items ===")

removed = inventory.remove_item(apple, 5)
print(f"Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(apple, 10)
print(f"Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(apple, 100)
print(f"Removed: {removed}")
print_inventory(inventory)

removed = inventory.remove_item(sword, 1)
print(f"Removed: {removed}")
print_inventory(inventory)