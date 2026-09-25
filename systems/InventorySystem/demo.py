from Inventory import Inventory
from ItemInstance import Item

sword = Item("Sword")
apple = Item("Apple")

inventory = Inventory()

inventory.add_item(sword)
inventory.add_item(sword)
inventory.add_item(apple, 3)

inventory.remove_item(sword)

slot = inventory.get_slot(apple)

print(slot.item.name)
print(slot.quantity)
